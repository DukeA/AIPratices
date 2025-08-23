import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'


# Load data
dataframe = pd.read_csv(url)


# Select first row
dataframe.iloc[0]