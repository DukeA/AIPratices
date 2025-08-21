import pandas as pd


url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/data.json'

dataframe = pd.read_json(url, orient='columns')


print(dataframe.head(2))