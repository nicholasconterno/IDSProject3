# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, corr

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("Analyze Player Statistics") \
    .getOrCreate()

# Define the paths for the Delta tables in DBFS
player_info_table_path = '/dbfs/mnt/delta/updated_player_info'
game_stats_table_path = '/dbfs/mnt/delta/game_stats'

# Load the Delta tables into Spark DataFrames
player_info_df = spark.read.format("delta").load(player_info_table_path)
game_stats_df = spark.read.format("delta").load(game_stats_table_path)

# Join the player_info_df and game_stats_df on 'id' to combine player information and game statistics
combined_df = player_info_df.join(game_stats_df, on='id', how='inner')

# Calculate correlations between 'r', 'h', and 'hr'
correlation_r = combined_df.corr('r', 'h')
correlation_h = combined_df.corr('h', 'hr')
correlation_hr = combined_df.corr('r', 'hr')

print("Correlation between 'r' and 'h':", correlation_r)
print("Correlation between 'h' and 'hr':", correlation_h)
print("Correlation between 'r' and 'hr':", correlation_hr)

# Find the player(s) with the highest 'r', 'h', and 'hr'
player_with_most_r = combined_df.orderBy(col('r').desc()).select('player', 'r').limit(5)
player_with_most_h = combined_df.orderBy(col('h').desc()).select('player', 'h').limit(5)
player_with_most_hr = combined_df.orderBy(col('hr').desc()).select('player', 'hr').limit(5)

print("Player(s) with the most 'r':")
player_with_most_r.show()

print("Player(s) with the most 'h':")
player_with_most_h.show()

print("Player(s) with the most 'hr':")
player_with_most_hr.show()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, corr


# Calculate correlations between 'r', 'h', and 'hr' and all other available statistics
correlation_with_r = {}
correlation_with_h = {}
correlation_with_hr = {}

# List of all available statistics columns (excluding 'r', 'h', and 'hr')
available_stats = [col_name for col_name in game_stats_df.columns if col_name not in ['id', 'year', 'team', 'r', 'h', 'hr']]

for stat in available_stats:
    correlation_with_r[stat] = game_stats_df.corr('r', stat)
    correlation_with_h[stat] = game_stats_df.corr('h', stat)
    correlation_with_hr[stat] = game_stats_df.corr('hr', stat)

# Find the statistic with the highest absolute correlation for 'r', 'h', and 'hr'
max_corr_with_r = max(correlation_with_r, key=lambda x: abs(correlation_with_r[x]))
max_corr_with_h = max(correlation_with_h, key=lambda x: abs(correlation_with_h[x]))
max_corr_with_hr = max(correlation_with_hr, key=lambda x: abs(correlation_with_hr[x]))

print("Statistics most correlated with 'r':", max_corr_with_r, "with correlation:", correlation_with_r[max_corr_with_r])
print("Statistics most correlated with 'h':", max_corr_with_h, "with correlation:", correlation_with_h[max_corr_with_h])
print("Statistics most correlated with 'hr':", max_corr_with_hr, "with correlation:", correlation_with_hr[max_corr_with_hr])





