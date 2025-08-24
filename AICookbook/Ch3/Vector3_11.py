# Load library
import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# Load data
dataframe = pd.read_csv(url)

# Delete column
dataframe.drop('Age', axis=1).head(2)

# Drop columns
dataframe.drop(['Age', 'Sex'], axis=1).head(2)

# Drop column
dataframe.drop(dataframe.columns[1], axis=1).head(2)

print(dataframe)

