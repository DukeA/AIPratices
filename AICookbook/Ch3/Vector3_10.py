# Load library
import numpy as np
import pandas as pd


# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# Load data
dataframe = pd.read_csv(url)


## Select missing values, show two rows
dataframe[dataframe['Age'].isnull()].head(2)


# Replace values with NaN
dataframe['Sex'] = dataframe['Sex'].replace('male', np.nan)


# Load data, set missing values
dataframe = pd.read_csv(url, na_values=[np.nan, 'NONE', -999])


# Get a single null row
null_entry = dataframe[dataframe["Age"].isna()].head(1)

print(null_entry)


# Fill all null values with the mean age of passengers
null_entry.fillna(dataframe["Age"].mean())