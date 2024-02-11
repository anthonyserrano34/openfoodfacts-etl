from scripts.load import load_data
from scripts.transform import clean_data
from scripts.generate_menu import generate_weekly_menu

# On charge les données dans des DataFrames
print("Loading data...")
openfoodfacts_df, diet_plans_df, users_df = load_data()

# On nettoie et traite les données
print("Cleaning data...")
clean_openfoodfacts_df = clean_data(openfoodfacts_df, diet_plans_df, users_df)

# On génère le menu hebdomadaire pour chaque utilisateur
print("Generating weekly menu...")
all_weekly_menus = generate_weekly_menu(users_df, diet_plans_df, clean_openfoodfacts_df)