import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# Load data
dataframe = pd.read_csv(url)

# Select unique values
dataframe['Sex'].unique()

pd.array(['female', 'male'], dtype=object)  

print(dataframe['Sex'].value_counts())


print(dataframe['PClass'].value_counts())