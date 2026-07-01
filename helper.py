import pandas as pd

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()

    df["Date"] = pd.to_datetime(df["Date"])
    df["Amount"] = pd.to_numeric(df["Amount"])

    df["Category"] = df["Category"].str.strip().str.title()
    df["Type"] = df["Type"].str.strip()

    return df


def create_features(df):
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    df["DayOfWeek"] = df["Date"].dt.day_name()

    return df