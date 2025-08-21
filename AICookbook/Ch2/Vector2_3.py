import pandas as pd 

url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/data.csv'

dataFrame = pd.read_csv(url)

print(dataFrame.head(10))