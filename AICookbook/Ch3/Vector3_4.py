# Load library
import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# Load data
dataframe = pd.read_csv(url)


# Show top two rows where column 'sex' is 'female'
print(dataframe[dataframe['Sex'] == 'female'].head(2))


# Filter rows
print(dataframe[(dataframe['Sex'] == 'female') & (dataframe['Age'] >= 65)])