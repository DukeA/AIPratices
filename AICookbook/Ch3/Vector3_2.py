import pandas as  pd

url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

dataframe = pd.read_csv(url)

print(dataframe.head(2))

print(dataframe.shape)

print(dataframe.describe())

print(dataframe.info())