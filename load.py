from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("OpenFoodFacts ETL") \
    .getOrCreate()

df = spark.read.option("delimiter", "\t").csv("csv/en.openfoodfacts.org.products.csv", header=True, inferSchema=True)

df.show()