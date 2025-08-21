import pandas as pd


url = (
    "https://docs.google.com/spreadsheets/d/"
    "1ehC-9otcAuitqnmWksqt1mOrTRCL38dv0K9UjhwzTOA/export?format=csv"
)

dataframe = pd.read_csv(url)


dataframe.head(2)