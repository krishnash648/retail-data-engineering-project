import logging

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# =========================================================
# Configure Logging
# =========================================================

logging.basicConfig(
    filename="logs/transformation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Transformation pipeline started")

# =========================================================
# Create Spark Session
# =========================================================

spark = SparkSession.builder \
    .appName("RetailDataTransformation") \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .getOrCreate()

# =========================================================
# Read Raw Dataset From Simulated S3 Raw Bucket
# =========================================================

df = spark.read.csv(
    "aws_s3_simulation/raw_bucket/online_retail.csv",
    header=True,
    inferSchema=True
)

# =========================================================
# Initial Dataset Count
# =========================================================

initial_count = df.count()

print("Initial Row Count:", initial_count)

logging.info(f"Initial Row Count: {initial_count}")

# =========================================================
# Data Cleaning
# =========================================================

# Remove rows with null customer IDs
df = df.dropna(subset=["CustomerID"])

# Remove duplicate rows
df = df.dropDuplicates()

# Remove invalid quantities
df = df.filter(col("Quantity") > 0)

# Remove invalid prices
df = df.filter(col("UnitPrice") > 0)

# Create total amount column
df = df.withColumn(
    "total_amount",
    col("Quantity") * col("UnitPrice")
)

# =========================================================
# Cleaned Dataset Count
# =========================================================

cleaned_count = df.count()

print("Cleaned Row Count:", cleaned_count)

logging.info(f"Cleaned Row Count: {cleaned_count}")

# =========================================================
# Preview Data
# =========================================================

df.show(5)

# =========================================================
# Convert Spark DataFrame to Pandas
# =========================================================

pandas_df = df.toPandas()

# =========================================================
# Save Cleaned CSV Into Processed Bucket
# =========================================================

pandas_df.to_csv(
    "aws_s3_simulation/processed_bucket/cleaned_retail.csv",
    index=False
)

logging.info("Processed CSV saved successfully")

print("Cleaned data saved successfully!")

logging.info("Transformation pipeline completed")

# =========================================================
# Stop Spark Session
# =========================================================

spark.stop()