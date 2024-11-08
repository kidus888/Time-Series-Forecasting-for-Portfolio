
import pandas as pd

def preprocess_data(df):
    """Preprocess data by handling missing values and ensuring correct types."""
    df.fillna(method='ffill', inplace=True)  # Fill missing values
    df.index = pd.to_datetime(df.index)      # Ensure index is datetime
    return df

def describe_data(df):
    """Display basic statistics of the data."""
    return df.describe()
