import pymysql
import pandas as pd


conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="db",
)

# Read the SQL query into a dataframe
dataframe = pd.read_sql("select * from data", conn)

# View the first two
dataframe.head(2)
