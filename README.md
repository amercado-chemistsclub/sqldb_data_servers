The ETL scripts are for inserting data into SQL Databases that include Postgresql and Google Cloud Spanner. The stock ticker data was obtained from an API such as Yahoo Finance using the Python Pandas Library. 
This is the API call from Pandas for a ticker such as AMD


import pandas_datareader as pdr
AMD = pdr.get_data_yahoo('AMD', start='2020-01-31')


The extracted data can be saved to a CSV file depending on the size of the dataset for future use. 
The interest rate data is historical and can be obtained from open sources. You can search for interest rate data  after logging in to their site: https://data.world/

Once the data is loaded into the databases, benchmark testing can be performed or further analytics scripts can be implemented such as forecasting. 
