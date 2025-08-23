import pandas as pd

# Create a dictionary
dictionary = {
    "Name": ["Jacky Jackson", "Steven Stevenson"],
    "Age": [38, 25],
    "Driver": [True, False],
}

# Create DataFrame
dataframe = pd.DataFrame(dictionary)

# Show DataFrame
print(dataframe)

dataframe["Eyes"] = ["Brown", "Blue"]

print(dataframe)
