import logging

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
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
    .getOrCreate()

# =========================================================
# Read Cleaned Dataset
# =========================================================

df = spark.read.csv(
    "data/processed/cleaned_retail.csv",
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
# Save Outputs Locally
# =========================================================

country_sales.toPandas().to_csv(
    "data/final/country_sales.csv",
    index=False
)

top_products.toPandas().to_csv(
    "data/final/top_products.csv",
    index=False
)

top_customers.toPandas().to_csv(
    "data/final/top_customers.csv",
    index=False
)

country_transactions.toPandas().to_csv(
    "data/final/country_transactions.csv",
    index=False
)

print("\nGold Layer Analytics Saved Successfully!")

logging.info("Gold layer analytics saved successfully")

logging.info("Gold layer analytics completed")

# =========================================================
# Stop Spark Session
# =========================================================

spark.stop()