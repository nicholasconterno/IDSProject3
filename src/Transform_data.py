# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("Transform Delta Table") \
    .getOrCreate()

# Define the path for the original Delta table in DBFS
original_table_path = 'dbfs:/dbfs/mnt/delta/baseball_delta_table'

# Read the original Delta table into a Spark DataFrame
original_df = spark.read.format("delta").load(original_table_path)

# Cast the 'id' column to the desired data type (e.g., IntegerType)
original_df = original_df.withColumn("id", col("id").cast("integer"))
original_df = original_df.withColumn("year", col("year").cast("integer"))
original_df = original_df.withColumn("stint", col("stint").cast("integer"))

# Select the relevant columns for player information
player_info_df = original_df.select("id", "player",
                                    "year", "stint", "team", "lg").distinct()

# Define the path for the new Delta table for player information
player_info_table_path = "/dbfs/mnt/delta/updated_player_info"

# Write the DataFrame to a Delta table for player information
player_info_df.write.format("delta").mode("overwrite").\
    save(player_info_table_path)

# Show the first few rows of the player information Delta table
player_info_df.show()
original_df = original_df.withColumn("id", col("id").cast("long"))
original_df = original_df.withColumn("year", col("year").cast("long"))
original_df = original_df.withColumn("stint", col("stint").cast("long"))
# Cast the 'id' column to the desired data type (e.g., Integ
game_stats_df = original_df.select(
    "id", "year", "team",  "r", "h", "X2b", "X3b", "hr", "rbi",
          "sb", "cs", "bb", "so", "ibb", "hbp", "sh", "sf", "gidp"
).distinct()

# Define the path for the Delta table for game statistics
game_stats_table_path = "/dbfs/mnt/delta/game_stats"

# Write the DataFrame to a Delta table for game statistics
game_stats_df.write.format("delta").mode("overwrite").\
    save(game_stats_table_path)

# Show the first few rows of the game statistics Delta table
game_stats_df.show()
