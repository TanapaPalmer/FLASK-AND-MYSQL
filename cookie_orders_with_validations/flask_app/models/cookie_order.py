from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Cookie_order:


    def __init__(self,cookie_order):

        self.id = cookie_order["id"]
        self.name = cookie_order["name"]
        self.cookie_type = cookie_order["cookie_type"]
        self.num_boxes = cookie_order["num_boxes"]
        self.created_at = cookie_order["created_at"]
        self.updated_at = cookie_order["updated_at"]

    @classmethod
    def is_valid(cls, cookie_order):
        valid = True

        if len(cookie_order["name"]) <= 0 or len(cookie_order["cookie_type"]) <= 0 or len(cookie_order["num_boxes"]) <= 0:
            valid = False
            flash("All fields required")
            return valid
        if len(cookie_order["name"]) < 2:
            valid = False
            flash("Name must be at least 2 characters")
        if len(cookie_order["cookie_type"]) < 2:
            valid = False
            flash("Cookie type must be at least 2 characters")
        if int(cookie_order["num_boxes"]) <= 0:
            valid = False
            flash("Please enter a valid number of boxes.")
        return valid
    
    @classmethod
    def get_by_id(cls, order_id):
        query = "SELECT * from cookie_orders WHERE id = %(id)s;"
        data = {
            "id": order_id
        }
        result = connectToMySQL('cookie_orders').query_db(query, data)
        if result:
            order = result[0]
            return order

        return False

    @classmethod
    def get_all(cls):
        query = "SELECT * from cookie_orders;"
        orders_data = connectToMySQL('cookie_orders').query_db(query)

        orders = []
        for order in orders_data:
            orders.append(cls(order))

        return orders

    @classmethod
    def create(cls, cookie_order):

        query = "INSERT into cookie_orders (name, cookie_type, num_boxes) VALUES (%(name)s, %(cookie_type)s, %(num_boxes)s);"

        result = connectToMySQL('cookie_orders').query_db(query, cookie_order)
        return result


    @classmethod
    def update(cls, cookie_order):

        query = "UPDATE cookie_orders SET name = %(name)s, cookie_type = %(cookie_type)s, num_boxes = %(num_boxes)s WHERE id = %(id)s;"

        result = connectToMySQL('cookie_orders').query_db(query, cookie_order)
        return result