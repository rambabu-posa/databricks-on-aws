# Databricks notebook source
# Import necessary libraries
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("ETL").getOrCreate()

# Read CSV data from S3 bucket
df = spark.read.csv("s3://bucket_name/input.csv", header=True, inferSchema=True)

# Perform ETL operations
# ...

# Write data as Parquet file into another S3 bucket
df.write.parquet("s3://bucket_name/output.parquet")

# Stop SparkSession
spark.stop()
