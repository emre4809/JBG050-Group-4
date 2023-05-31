
import pandas as pd
import numpy as np

def process_data():
    print("processing and restructuring data...")
    df = pd.read_pickle("burglaries_barnet_df.pickle")
    LSOA_list = df["LSOA_code"].unique()

    df_LSOA_per_month = pd.DataFrame(LSOA_list, columns=["LSOA"]).set_index("LSOA")
    months = np.array(df["Month"].unique())
    months.sort()
    dict_lsoa_per_month = {}
    for cur_month in months:
        df_month = df[df["Month"] == cur_month].copy()

        # prevent counting same crime id twice
        df_month = df_month[["LSOA_code", "Crime_ID"]].drop_duplicates().groupby("LSOA_code").count()
        df_month = df_month.reindex(LSOA_list).fillna(0)
        df_month = df_month.rename(columns={"Crime_ID": cur_month})
        df_LSOA_per_month = pd.concat([df_LSOA_per_month, df_month], axis=1)

    df_LSOA_per_month = df_LSOA_per_month.reindex(sorted(df_LSOA_per_month.columns), axis=1).sort_index()
    df_LSOA_per_month.to_pickle("barnet_burglaries_agg_df.pickle")
    print("DONE, ", "barnet_burglaries_agg_df.pickle")


