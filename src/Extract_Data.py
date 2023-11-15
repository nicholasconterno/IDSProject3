# Databricks notebook source
import requests
import pandas as pd
from io import StringIO
from pyspark.sql import SparkSession
# URL of the CSV file
csv_url = 'https://raw.githubusercontent.com/pandas-dev/'
csv_url += 'pandas/main/doc/data/baseball.csv'

# Fetch CSV data using requests
response = requests.get(csv_url)
response.raise_for_status()  # Ensure the request was successful

# Convert the CSV data to a Pandas DataFrame
pd_df = pd.read_csv(StringIO(response.text))

spark = SparkSession.builder \
    .appName("Write Pandas DataFrame to Delta Lake") \
    .getOrCreate()

# Define the path for the Delta table in DBFS
delta_table_path = '/dbfs/mnt/delta/baseball_delta_table'

# Convert the Pandas DataFrame to a Spark DataFrame
df = spark.createDataFrame(pd_df)

# Write the DataFrame to a Delta table
df.write.format("delta").mode("overwrite").save(delta_table_path)

# Show the first few rows of the Delta table
df.show()
