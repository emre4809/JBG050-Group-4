import numpy as np

def clean_data(df, modes=[1]):
    """
    Cleans the dataset in a chosen way:
    1: deletes one-to-one duplicate entries (same entries across all columns)
    2: deletes duplicate Crime IDs (keeps the most important outcome)
    3: deletes empty entries in a chosen column(s)
    """
    if 1 in modes:
        df = df.drop_duplicates()
    if 2 in modes:
        best =  ['Investigation complete; no suspect identified', 'Offender given a caution', 'Offender given penalty notice', 
                 'Local resolution', 'Offender given a drugs possession warning', 'Awaiting court outcome',
                 'Suspect charged as part of another case', 'Formal action is not in the public interest']
        medium = ['Awaiting court outcome', 'Under investigation', 'Unable to prosecute suspect']
        worst = ['Court result unavailable', 'Status update unavailable', None]
        conditions = [df['Last outcome category'].isin(best),
            df['Last outcome category'].isin(medium),
            df['Last outcome category'].isin(worst)]
        scores = [1, 2, 3]

        df['outcome_score'] = np.select(conditions, scores, default=0)
        df = df.sort_values(['outcome_score', 'Crime ID'], ascending=True)
        columns = ['Month','Reported by','Falls within','Longitude','Latitude','Location','LSOA code','LSOA name','Crime type']
        df = df.drop_duplicates(subset=columns, keep='first')
        df = df.drop('outcome_score', axis=1)
        df = df.sort_index()
    if 3 in modes:
        col_name = 'Longitude' # Your column(s) name
        df = df.dropna(subset=[col_name])
        df = df.reset_index(drop=True)

    return df
