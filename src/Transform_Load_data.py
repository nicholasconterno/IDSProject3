# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("Transform Delta Table with Spark SQL") \
    .getOrCreate()

# Define the path for the original Delta table in DBFS
original_table_path = 'dbfs:/dbfs/mnt/delta/baseball_delta_table'

try:
    # Read the original Delta table into a Spark DataFrame
    original_df = spark.read.format("delta").load(original_table_path)
    if original_df.rdd.isEmpty():
        raise ValueError("The DataFrame is empty. Check your data source.")

    # Register DataFrame as a temporary view
    original_df.createOrReplaceTempView("original_data")

    # Using Spark SQL to transform the data
    transformed_df = spark.sql("""
        SELECT
            CAST(id AS INTEGER) AS id,
            player,
            CAST(year AS INTEGER) AS year,
            CAST(stint AS INTEGER) AS stint,
            team,
            lg
        FROM original_data
    """)

    # Define the path for the new Delta table for player information
    player_info_table_path = "/dbfs/mnt/delta/updated_player_info"

    # Write the transformed DataFrame to a Delta table for player information
    transformed_df.write.format("delta").\
        mode("overwrite").save(player_info_table_path)

    # Show the first few rows of the player information Delta table
    transformed_df.show()

    # Register transformed DataFrame as a temporary vin
    transformed_df.createOrReplaceTempView("transformed_data")

    # Perform additional transformations using Spark SQL
    game_stats_df = spark.sql("""
        SELECT
            id,
            year,
            team,
            r,
            h,
            X2b,
            X3b,
            hr,
            rbi,
            sb,
            cs,
            bb,
            so,
            ibb,
            hbp,
            sh,
            sf,
            gidp
        FROM transformed_data
    """)

    # Define the path for the Delta table for game statistics
    game_stats_table_path = "/dbfs/mnt/delta/game_stats"

    # Write the DataFrame to a Delta table for game statistics
    game_stats_df.write.format("delta").\
        mode("overwrite").save(game_stats_table_path)

    # Show the first few rows of the game statistics Delta table
    game_stats_df.show()

except AnalysisException as e:
    # Handle exceptions related to DataFrame operations
    print(f"An error occurred during DataFrame operations: {e}")

except Exception as e:
    # Handle any other exceptions
    print(f"An error occurred: {e}")
