import pandas as pd

from helper import clean_data
from helper import create_features

def load_data():

    df = pd.read_csv("Personal_Finance_Dataset.csv")

    df = clean_data(df)

    df = create_features(df)

    return df