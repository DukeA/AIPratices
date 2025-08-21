
import pandas as pd
from sqlalchemy import create_engine


database_connection = create_engine('sqlite:///sample.db')


dataframe = pd.read_sql_query('SELECT * FROM data', database_connection)


dataframe.head(2)