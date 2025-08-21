import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/data.xlsx'

dataframe = pd.read_csv(url, sheet_name =0, header=0)

print(dataframe.head(2))