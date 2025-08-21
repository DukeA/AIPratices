import pandas as pd

# Create URL
url = 'https://machine-learning-python-cookbook.s3.amazonaws.com/data.parquet'

# Load data

dataframe = pd.read_parquet(url)

# View the first two rows
dataframe.head(2)