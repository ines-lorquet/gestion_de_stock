import mysql.connector

class Product_Manager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="azerty",
            database="store"
        )
        self.cursor = self.connection.cursor()

    def add_product(self, name, description, price, quantity, id_category):
        sql = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
        values = (name, description, price, quantity, id_category)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def name_product(self):
        sql = "SELECT name FROM product"
        self.cursor.execute(sql)
        self.names = self.cursor.fetchall()
        return self.names
    
    def description_product(self):
        sql = "SELECT description FROM product"
        self.cursor.execute(sql)
        self.description = self.cursor.fetchall()
        return self.description


    def delete_product(self, product_id):
        sql = "DELETE FROM product WHERE id = %s"
        values = (product_id,)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def modify_product(self, product_id, new_product):
        set_clause = ", ".join([f"{key} = '{value}'" for key, value in new_product.items()])
        sql = f"UPDATE product SET {set_clause} WHERE id = %s"
        self.cursor.execute(sql, (product_id,))
        self.connection.commit()

    def display_product(self):
        sql = "SELECT * FROM product"
        self.cursor.execute(sql)
        products = self.cursor.fetchall()
        for product in products:
            print(product)
            
    def display_product_in_category(self):
        sql = "SELECT product.id, product.name, product.description, product.price, product.quantity, product.id_category FROM product LEFT JOIN category ON category.id = product.id_category"
        self.cursor.execute(sql)
        produit_available = self.cursor.fetchall()
        
    def close_connection(self):
        self.cursor.close()
        self.connection.close()

product_manager = Product_Manager()
# product_manager.add_product("Sauce Nuoc-mam", "", 15, 30, 2)
# product_manager.add_product("Sauce Hoisin", "", 15, 30, 2)
# product_manager.add_product("Sauce Srirahca", "", 15, 30, 2)

# product_manager.modify_product(8, {'name': 'Sauce Sriracha piquante'})
# product_manager.delete_product(11)
product_manager.delete_product(13)
product_manager.display_product()
# product_manager.display_product_in_category()
# product_manager.close_connection()