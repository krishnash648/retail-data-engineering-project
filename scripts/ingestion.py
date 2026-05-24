from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("RetailETLPipeline") \
    .getOrCreate()

# Read CSV
df = spark.read.csv(
    "data/raw/online_retail.csv",
    header=True,
    inferSchema=True
)

# Show first rows
df.show(5)

# Print schema
df.printSchema()

# Print total rows
print("Total Rows:", df.count())

# Stop Spark
spark.stop()