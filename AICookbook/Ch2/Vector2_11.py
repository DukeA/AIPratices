import pandas as pd


s3_uri = "s3://machine-learning-python-cookbook/data.csv"


ACCESS_KEY_ID = "xxxxxxxxxxxxx"
SECRET_ACCESS_KEY = "xxxxxxxxxxxxxxxx"


dataframe = pd.read_csv(
    s3_uri,
    storage_options={
        "key": ACCESS_KEY_ID,
        "secret": SECRET_ACCESS_KEY,
    },
)
# View first two rows
dataframe.head(2)
