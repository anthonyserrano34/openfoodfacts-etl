import mysql.connector

def connect_to_mysql(host, user, password, database):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection

def insert_weekly_menus_to_mysql(connection, all_weekly_menus):
    cursor = connection.cursor()
    for weekly_menu in all_weekly_menus:
        for daily_menu in weekly_menu:
            query = """
                INSERT INTO weekly_menus (user_id, day, breakfast_product, lunch_product, dinner_product)
                VALUES (%s, %s, %s, %s, %s)
            """
            data = (
                daily_menu["user_id"],
                daily_menu["day"],
                daily_menu["breakfast_product"],
                daily_menu["lunch_product"],
                daily_menu["dinner_product"]
            )
            cursor.execute(query, data)
    connection.commit()
    cursor.close()