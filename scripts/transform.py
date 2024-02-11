from pyspark.sql.functions import col

def clean_data(openfoodfacts_df, diet_plans_df, users_df):
    # On filtre les produits qui ne contiennent pas les informations nutritionnelles nécessaires (énergie, protéines, graisses, glucides)
    openfoodfacts_df = openfoodfacts_df.filter(
        col("energy-kcal_100g").isNotNull() &
        col("proteins_100g").isNotNull() &
        col("fat_100g").isNotNull() &
        col("carbohydrates_100g").isNotNull()
    )

    # On filtre les produits qui contiennent des valeurs aberrantes pour les informations nutritionnelles en utilisant des bornes supérieures pour chaque colonne ou inférieur à 0
    energy_upper_limit = 10000
    proteins_upper_limit = 1000
    fat_upper_limit = 1000
    carbohydrates_upper_limit = 1000
    openfoodfacts_df = openfoodfacts_df.filter(
        (col("energy-kcal_100g") > 0) &
        (col("energy-kcal_100g") <= energy_upper_limit) &
        (col("proteins_100g") > 0) &
        (col("proteins_100g") <= proteins_upper_limit) &
        (col("fat_100g") > 0) &
        (col("fat_100g") <= fat_upper_limit) &
        (col("carbohydrates_100g") > 0) &
        (col("carbohydrates_100g") <= carbohydrates_upper_limit)
    )

    # On fait une jointure entre les DataFrames openfoodfacts_df et users_df pour filtrer les produits par pays en utilisant la colonne "country" du DataFrame users_df et la colonne "countries_en" du DataFrame openfoodfacts_df, et on filtre les produits sans nom ou non disponibles dans la région de l'utilisateur
    users_df.select("country").show()
    joined_df = openfoodfacts_df.join(
        users_df, openfoodfacts_df["countries_en"] == users_df["country"], "inner")
    openfoodfacts_df = joined_df.filter(
        (joined_df["product_name"].isNotNull()) &
        (joined_df["countries_en"].isNotNull())
    )

    # On supprime les doublons des produits en utilisant les colonnes "product_name" et "countries_en"
    openfoodfacts_df = openfoodfacts_df.dropDuplicates(
        ["product_name", "countries_en"])

    # On sélectionne les colonnes nécessaires pour l'analyse (nom du produit, énergie, protéines, graisses, glucides, pays)
    openfoodfacts_df = openfoodfacts_df.select(
        "product_name", "energy-kcal_100g", "proteins_100g", "fat_100g", "carbohydrates_100g", "countries_en"
    )
    openfoodfacts_df.show()

    return openfoodfacts_df
