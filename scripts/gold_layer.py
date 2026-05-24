import logging

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    sum,
    count,
    desc
)

# =========================================================
# Configure Logging
# =========================================================

logging.basicConfig(
    filename="logs/gold_layer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Gold layer analytics started")

# =========================================================
# Create Spark Session
# =========================================================

spark = SparkSession.builder \
    .appName("RetailGoldLayer") \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .getOrCreate()

# =========================================================
# Read Cleaned Dataset From Processed Bucket
# =========================================================

df = spark.read.csv(
    "aws_s3_simulation/processed_bucket/cleaned_retail.csv",
    header=True,
    inferSchema=True
)

print("Cleaned Dataset Loaded")

logging.info("Cleaned dataset loaded successfully")

# =========================================================
# 1. Country-wise Revenue
# =========================================================

country_sales = df.groupBy("Country") \
    .agg(
        sum("total_amount").alias("total_revenue")
    ) \
    .orderBy(desc("total_revenue"))

print("\nTop Countries by Revenue")

country_sales.show(10)

logging.info("Country sales analytics completed")

# =========================================================
# 2. Top Selling Products
# =========================================================

top_products = df.groupBy("Description") \
    .agg(
        sum("Quantity").alias("total_quantity_sold")
    ) \
    .orderBy(desc("total_quantity_sold"))

print("\nTop Selling Products")

top_products.show(10)

logging.info("Top products analytics completed")

# =========================================================
# 3. Top Customers
# =========================================================

top_customers = df.groupBy("CustomerID") \
    .agg(
        sum("total_amount").alias("customer_revenue")
    ) \
    .orderBy(desc("customer_revenue"))

print("\nTop Customers")

top_customers.show(10)

logging.info("Top customers analytics completed")

# =========================================================
# 4. Transaction Count by Country
# =========================================================

country_transactions = df.groupBy("Country") \
    .agg(
        count("InvoiceNo").alias("transaction_count")
    ) \
    .orderBy(desc("transaction_count"))

print("\nTransactions by Country")

country_transactions.show(10)

logging.info("Country transactions analytics completed")

# =========================================================
# Convert Spark DataFrames to Pandas
# =========================================================

country_sales_pd = country_sales.toPandas()

top_products_pd = top_products.toPandas()

top_customers_pd = top_customers.toPandas()

country_transactions_pd = country_transactions.toPandas()

# =========================================================
# Save Outputs Into Gold Bucket
# =========================================================

country_sales_pd.to_csv(
    "aws_s3_simulation/gold_bucket/country_sales.csv",
    index=False
)

top_products_pd.to_csv(
    "aws_s3_simulation/gold_bucket/top_products.csv",
    index=False
)

top_customers_pd.to_csv(
    "aws_s3_simulation/gold_bucket/top_customers.csv",
    index=False
)

country_transactions_pd.to_csv(
    "aws_s3_simulation/gold_bucket/country_transactions.csv",
    index=False
)

print("\nGold Layer Analytics Saved Successfully!")

logging.info("Gold layer analytics saved successfully")

logging.info("Gold layer analytics completed")

# =========================================================
# Stop Spark Session
# =========================================================

spark.stop()