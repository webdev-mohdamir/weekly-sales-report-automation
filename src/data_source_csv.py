import pandas as pd


def load_data_from_csv(filepath="data/sales_data.csv"):
    df = pd.read_csv(filepath)
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], format="%d-%m-%Y")
    return df
