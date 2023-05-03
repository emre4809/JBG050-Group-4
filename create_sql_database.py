import pandas as pd
import sqlite3
import os
import time

start = time.time()

database_path = "database.sqlite"
data_path = "base/"
crimes_columns = ['Crime ID', 'Month', 'Reported by', 'Falls within', 'Longitude',
       'Latitude', 'Location', 'LSOA code', 'LSOA name', 'Crime type',
       'Last outcome category', 'Context']
# todo define dtypes here if necessary
crimes_dtypes = {c:"" for c in crimes_columns}

def create_db():
    """
    Creates initial empty database with tables.

    Returns
    -------
        db: sqlite.db
        The sqlite database that was created. Use db.cursor() to get a
        cursor which can be used to execute sql with.

    """
    def get_table_creation_prompt(tablename:str, d:dict):
        table = """ CREATE TABLE %s (""" % tablename
        first_col = True
        for col in d:
            if first_col:
                table += "\n\"%s\" %s" % (col, d[col])
            else:
                table += ",\n\"%s\" %s" % (col, d[col])
            first_col = False
        table += """\n); """
        return table
    base_prompt = get_table_creation_prompt("CRIMES", crimes_dtypes)
    
    if os.path.exists(database_path):
        os.remove(database_path)
    db = sqlite3.connect(database_path)
    cur = db.cursor()
    cur.execute(base_prompt)
    
    print(base_prompt)
    return db


def insert_street_file(filepath, cur):
    """
    Inserts a given csv file found at filepath into the database linked
    to the given cursor.

    Parameters
    ----------
    filepath : TYPE
        full filepath from this script to a .csv file.
    cur : TYPE
        db.cursor()

    Returns
    -------
    None.

    """
    print("inserting ", filepath)
    df = pd.read_csv(filepath)
    df.to_sql(name="TEMP_CRIMES", con=db, index=False, if_exists='replace')
    cur.execute("INSERT OR IGNORE INTO CRIMES SELECT * FROM TEMP_CRIMES")


db = create_db()
cur = db.cursor()
date_folders = os.listdir(data_path)
for folder in date_folders:
    for file in os.listdir(data_path+folder):
        # the other types of files can be added here
        if "-street.csv" in file:
            insert_street_file(data_path+folder+"/"+file, cur)
            db.commit()
cur.execute("DROP TABLE TEMP_CRIMES")
print("took", round(time.time() - start), "seconds")
db.close()
