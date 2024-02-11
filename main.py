from scripts.load import load_data

# On charge les données dans des DataFrames
print("Loading data...")
openfoodfacts_df, diet_plans_df, users_df = load_data()