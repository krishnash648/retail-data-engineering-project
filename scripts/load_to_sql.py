import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("retail_analytics.db")

# Load datasets
country_sales = pd.read_csv("data/final/country_sales.csv")
top_products = pd.read_csv("data/final/top_products.csv")
top_customers = pd.read_csv("data/final/top_customers.csv")
country_transactions = pd.read_csv("data/final/country_transactions.csv")

# Store tables in SQLite
country_sales.to_sql(
    "country_sales",
    conn,
    if_exists="replace",
    index=False
)

top_products.to_sql(
    "top_products",
    conn,
    if_exists="replace",
    index=False
)

top_customers.to_sql(
    "top_customers",
    conn,
    if_exists="replace",
    index=False
)

country_transactions.to_sql(
    "country_transactions",
    conn,
    if_exists="replace",
    index=False
)

print("Data loaded into SQLite successfully!")

conn.close()