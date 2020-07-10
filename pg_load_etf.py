import numpy as np

import pandas as pd

data = pd.read_csv("tech_stocks_history.csv")
rates_yr = pd.read_csv("interest_rates_history.csv")

import psycopg2
from sqlalchemy import create_engine

from sqlalchemy_utils import create_database, database_exists, drop_database

# Create the connection to a new etfdb postgres instance based on the docker run parameters
engine = create_engine('postgresql://postgres:cybercoders@localhost/etfdb')
# If a PostgreSQL database with this name exists
if database_exists(engine.url):
    # Delete PostgreSQL database
    drop_database(engine.url)
    # Create empty PostgreSQL database
    create_database(engine.url)
# Otherwise
else:
    # Create empty PostgreSQL database
    create_database(engine.url)

from sqlalchemy.types import Integer, String, Float, Date

# Insert whole DataFrame into MySQL

data.to_sql('tech_stocks', engine, if_exists='append', index=False, dtype={"Date": Date(), "SP500": Float(), "AAPL": Float(),"GOOG": Float(),"AMZN": Float(),"NVDA": Float(),"TSLA": Float(),"MSFT": Float()})
rates_yr.to_sql('interest_yr', engine, if_exists='append', index=False, dtype={"Date": Date(), "OneMO": Float(), "ThreeMO": Float(),"SixMO": Float(),"OneYR": Float()})
