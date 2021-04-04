The ETL scripts are for inserting data into SQL Databases that include Postgresql and Google Cloud Spanner. The stock ticker data was obtained from an API such as Yahoo Finance using the Python Pandas Library. 
This is the API call from Pandas for a ticker such as AMD


import pandas_datareader as pdr


AMD = pdr.get_data_yahoo('AMD', start='2020-01-31')


The extracted data can be saved to a CSV file depending on the size of the dataset for future use. 
The interest rate data is historical and can be obtained from open sources. You can search for interest rate data  after logging in to their site: https://data.world/

Once the data is loaded into the databases, benchmark testing can be performed or further analytics scripts can be implemented such as forecasting. The python code for forecasting future prices using the H2O.ai library can be downloaded and imported into a Google colab session as a notebook. You can change it for different stock tickers of interest.

In order to install Postgres on your local machine for this example, go to the Dockerhub and run the commands for pulling the Docker image from  their registry:https://hub.docker.com/_/postgres

In order to use Google Cloud Spanner, refer to their documentation on how to set up an instance on Google Cloud. 
https://cloud.google.com/spanner/docs/quickstart-console

In order to install and run code in the H2O.ai framework refer to their documentation.
https://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html
