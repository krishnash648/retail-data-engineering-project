import logging

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Configure logging
logging.basicConfig(
    filename="logs/transformation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Transformation pipeline started")

# Create Spark Session
spark = SparkSession.builder \
    .appName("RetailDataTransformation") \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .getOrCreate()

# Read raw data
df = spark.read.csv(
    "data/raw/online_retail.csv",
    header=True,
    inferSchema=True
)

# Initial row count
initial_count = df.count()

print("Initial Row Count:", initial_count)

logging.info(f"Initial Row Count: {initial_count}")

# Remove rows where CustomerID is null
df = df.dropna(subset=["CustomerID"])

# Remove duplicate rows
df = df.dropDuplicates()

# Remove invalid quantities
df = df.filter(col("Quantity") > 0)

# Remove invalid prices
df = df.filter(col("UnitPrice") > 0)

# Create total_amount column
df = df.withColumn(
    "total_amount",
    col("Quantity") * col("UnitPrice")
)

# Cleaned row count
cleaned_count = df.count()

print("Cleaned Row Count:", cleaned_count)

logging.info(f"Cleaned Row Count: {cleaned_count}")

# Show transformed data
df.show(5)

# Convert Spark DataFrame to Pandas
pandas_df = df.toPandas()

# Save cleaned data
pandas_df.to_csv(
    "data/processed/cleaned_retail.csv",
    index=False
)

print("Cleaned data saved successfully!")

logging.info("Cleaned data saved successfully")

logging.info("Transformation pipeline completed")

# Stop Spark Session
spark.stop()