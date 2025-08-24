import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'


# Load data
dataframe = pd.read_csv(url)


# Select first row
dataframe.iloc[0]


dataframe.iloc[1:4]

dataframe.iloc[:4]


dataframe = dataframe.set_index(dataframe["Name"])


dataframe.loc["Allen, Miss Elisabeth Walton"]
