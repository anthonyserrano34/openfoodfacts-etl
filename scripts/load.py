from pyspark.sql import SparkSession

def load_data():
    spark = SparkSession.builder \
        .appName("OpenFoodFacts ETL") \
        .getOrCreate()
        
    # On charge les données des produits Open Food Facts
    openfoodfacts_df = spark.read.option("delimiter", "\t").csv(
        "csv/en.openfoodfacts.org.products.csv", header=True, inferSchema=True)
    
    openfoodfacts_df.printSchema()
    
    # On charge les données des régimes alimentaires
    diet_plans_df = spark.read.csv(
        "csv/diet_plans.csv", header=True, inferSchema=True)
    
    diet_plans_df.printSchema()
    
    # On charge les données des utilisateurs
    users_df = spark.read.csv("csv/users.csv", header=True, inferSchema=True)
    users_df.printSchema()
    
    return openfoodfacts_df, diet_plans_df, users_df