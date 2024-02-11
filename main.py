from scripts.load import load_data
from scripts.transform import clean_data

# On charge les données dans des DataFrames
print("Loading data...")
openfoodfacts_df, diet_plans_df, users_df = load_data()

# On nettoie et traite les données
print("Cleaning data...")
clean_openfoodfacts_df = clean_data(openfoodfacts_df, diet_plans_df, users_df)