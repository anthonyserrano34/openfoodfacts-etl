from scripts.load import load_data
from scripts.transform import clean_data
from scripts.generate_menu import generate_weekly_menu
from scripts.extract import connect_to_mysql, insert_weekly_menus_to_mysql

# On charge les données dans des DataFrames
print("Loading data...")
openfoodfacts_df, diet_plans_df, users_df = load_data()

# On nettoie et traite les données
print("Cleaning data...")
clean_openfoodfacts_df = clean_data(openfoodfacts_df, diet_plans_df, users_df)

# On génère le menu hebdomadaire pour chaque utilisateur
print("Generating weekly menu...")
all_weekly_menus = generate_weekly_menu(users_df, diet_plans_df, clean_openfoodfacts_df)

# On extrait les données dans la base de données MySQL
print("Extracting data...")
connection = connect_to_mysql("localhost", "root", "root", "datawarehouse")
insert_weekly_menus_to_mysql(connection, all_weekly_menus)
connection.close()