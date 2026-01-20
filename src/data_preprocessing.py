import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess(data):
    X = data[['day']]
    y = data['items_sold']
    return X, y
