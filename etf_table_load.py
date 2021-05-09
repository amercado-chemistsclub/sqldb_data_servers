#Script Loads table data from a csv file into a Spanner Instance

# csv file is from Github repo for sqkdb
!wget https://raw.githubusercontent.com/amercado-chemistsclub/sqldb_data_servers/master/tech_stocks_history.csv

from google.cloud import spanner
from google.cloud.spanner import Client
import pandas as pd

#Read the csv file and select columns into a dataframe
df_tech = pd.read_csv("tech_stocks_history.csv")
df = df_tech[['Date','NVDA','TSLA']]

#Connect to the Spanner instance and database that were set up
instance_id = 'spanner-ETFtest'
instance = spanner_client.instance(instance_id)

database_id = 'historical_etf'
database = instance.database(database_id)

#Instead of row by row insertion run the batch load as a list
columns = df.columns
values = df.values.tolist()

#Insert the data into the table specifed with the batch method
with database.batch() as batch:
    batch.insert(
        table='Stock_past',
        columns=columns,
        values=values
    )

#Afterwords view the data inserted on the GCP Spanner cosole
