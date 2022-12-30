import pandas as pd
import config


def load_data(filepath=None):
    df = pd.read_csv(filepath)
    return df


def find_part(part, df):
    part_df = df[df["competitor_part"] == part]
    return part_df
def save_df(df=None):
    df.to_excel
