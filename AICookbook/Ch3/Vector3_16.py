# Load library
import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# Load data
dataframe = pd.read_csv(url)

# Get the minimum of every column
min =dataframe.agg("min")
print(min)


dataframe.agg({"Age":["mean"], "SexCode":["min", "max"]})


dataframe.groupby(
["PClass","Survived"]).agg({"Survived":["count"]}
).reset_index()