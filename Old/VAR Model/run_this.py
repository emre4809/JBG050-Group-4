import pandas as pd
import sqlite3
import os
import _data_processing
import _models
from os.path import exists

"""Connect to the sql database"""
database_path = "../crimes.db"
if not exists("burglaries_barnet_df.pickle"):
    assert(os.path.exists(database_path)), "this notebook requires 'crimes.db' a sqlite database that at minimum contains all" \
                                           " burglaries that took place in Barnet from years 2010 up to 2023 \n "\
                                           " See readme for more information on how to obtain the database."
    print("connecting to, ", database_path)
    db = sqlite3.connect(database_path)
    cur = db.cursor()
    """Read to dataframe"""
    print("getting only burglaries in Barnet, this might take a while if the database contains many other crimes")
    df = pd.read_sql("""SELECT * 
                    FROM crimes
                    WHERE "LSOA_name" LIKE 'Barnet%'
                    AND "Crime_type" LIKE 'Burglary'""", con=db)
    print("storing results temporarily in burglaries_barnet_df.pickle")
    cur.close()
    df.to_pickle("burglaries_barnet_df.pickle")
    print("done")

_data_processing.process_data()
_models.fit_and_test()