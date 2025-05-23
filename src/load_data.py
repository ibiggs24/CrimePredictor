# Functions for reading/cleaning data
import pandas as pd

def load_crime_data(path):
    df = pd.read_csv(path)
    print("Loaded data with shape: ", df.shape)
    return df