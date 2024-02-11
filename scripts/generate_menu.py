def generate_daily_menu(diet_plan, available_products):
    # On sélectionne les produits disponibles et qui sont ok avec le régime alimentaire
    print(diet_plan)
    filtered_products = available_products.filter(
        (available_products["carbohydrates_100g"] <= diet_plan["carbohydrates_max_g"]) &
        (available_products["proteins_100g"] >= diet_plan["protein_min_g"]) &
        (available_products["fat_100g"] <= diet_plan["fat_max_g"]) &
        (available_products["energy-kcal_100g"] <= diet_plan["max_calories_kcal"])
    )
    # Puis on sélectionne un produit aléatoire pour chaque repas (petit déjeuner, déjeuner, dîner)
    breakfast = filtered_products.sample(withReplacement=False, fraction=0.1).first()
    lunch = filtered_products.sample(withReplacement=False, fraction=0.1).first()
    dinner = filtered_products.sample(withReplacement=False, fraction=0.1).first()
    print(breakfast, lunch, dinner)
    return breakfast, lunch, dinner

def generate_weekly_menu(user_df, diet_plans_df, clean_openfoodfacts_df):
    all_weekly_menus = []
    
    # On créer une boucle à travers chaque utilisateur du DataFrame user_df
    for user_info in user_df.collect():
        # On récupère l'identifiant et le régime alimentaire de l'utilisateur
        user_id = user_info["user_id"]
        user_diet_plan = user_info["diet_plan"]
        user_df.show()
        print(user_id, user_diet_plan)
        diet_plan_info = diet_plans_df.filter(diet_plans_df["diet_plan"] == user_diet_plan).first()
        print(diet_plan_info)

        # On génère un menu hebdomadaire pour l'utilisateur en utilisant la fonction generate_daily_menu et on l'ajoute à la liste all_weekly_menus
        weekly_menu = []
        for day in range(1, 8):
            print(day)
            breakfast, lunch, dinner = generate_daily_menu(diet_plan_info, clean_openfoodfacts_df)
            daily_menu = {
                "user_id": user_id,
                "day": day,
                "breakfast_product": breakfast.product_name,
                "lunch_product": lunch.product_name,
                "dinner_product": dinner.product_name
            }
            weekly_menu.append(daily_menu)
        
        # On ajoute le menu hebdomadaire à la liste all_weekly_menus et on passe à l'utilisateur suivant dans la boucle
        all_weekly_menus.append(weekly_menu)

    return all_weekly_menus
