# ADMIN INTERFACE
from datetime import datetime
import psycopg2
from config import *
from connection import Connection


class Admin(Connection):
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def register_self(self):
        self.register(self.login, self.password, 'adm')

    def login_self(self):
        return self.login_check(self.login, self.password, 'adm')

    def add_product(self, data):
        table = 'product'
        result = self.postData(table, data)
        return result

    def add_product_category(self, data):
        table = 'product_category'
        result = self.postData(table, data)
        return result

    def add_employee(self, login, password, first_name, last_name, city, day_of_birth, chief):
        if self.login_self():
            role = 'emp'
            self.register(login, password, role)

    def delete_product(self, selector):
        table = 'product'
        selector = f"product_name = '{selector}'"
        result = self.deleteData(self, table, selector)
        return result

    def delete_product_category(self, selector):
        table = 'product_category'
        selector = f"category_name = '{selector}'"
        result = self.deleteData(self, table, selector)
        return result

    def delete_employee(self, selector):
        table = 'employee'
        selector = f"id = '{selector}'"
        result = self.deleteData(self, table, selector)
        return result

    def delete_customer(self, selector):
        table = 'customer'
        selector = f"id = '{selector}'"
        result = self.deleteData(self, table, selector)
        return result

    def edit_product(self, data, selector):
        table = 'product'
        result = self.updateData(table, data, selector)
        return result

    def edit_product_category(self, data, selector):
        table = 'product_category'
        result = self.updateData(table, data, selector)
        return result

    def edit_employee(self):
        pass

    def get_order_info(self, category='', selector='', ):
        """
        category must be one of the item from the list:
        ['city_name','date_of_order', 'product_name']
        date format for selector: 2020-6-12
        """
        if self.login_self():
            categoryes = ['city_name', 'date_of_order',
                          'product_name', 'status']
            table = ('orders o',)
            fields = ("""o.id, concat(e.first_name,' ', e.last_name) as "employee", c.city_name, o.date_of_order, concat(c2.first_name,' ', c2.last_name) as "customer", p.product_name, o.price """,)
            if category and category in categoryes and selector != '':
                selector = selector if isinstance(
                    selector, bool) == bool else str(selector)
                where = f"""where {category} = {selector}"""
            else:
                where = ''
            selector = f""" left JOIN employee e on e.id = o.employee_id 
                            left JOIN city c on c.id = o.city_id 
                            left JOIN customer c2 on c2.id = o.customer_id 
                            left JOIN product p on p.id = o.product_id {where}"""
            result = self.getData(table, fields, selector)
            fieldNames = ["id", "employee", "city_name",
                          "date_of_order", "customer", "product_name", "price"]
            changeRes = []
            for item in result:
                cort = {}
                for index, element in enumerate(item):
                    cort[fieldNames[index]] = element
                changeRes.append(cort)
        else:
            changeRes = "Invalid loging!"
        return changeRes

    def get_city(self, selector):
        if self.login_self():
            table = ('orders o',)
            fields = ("""o.id, concat(e.first_name,' ', e.last_name) as "employee", c.city_name, o.date_of_order, concat(c2.first_name,' ', c2.last_name) as "customer", p.product_name, o.price, o.status """,)
            selector = f""" left JOIN employee e on e.id = o.employee_id 
                            left JOIN city c on c.id = o.city_id 
                            left JOIN customer c2 on c2.id = o.customer_id 
                            left JOIN product p on p.id = o.product_id,
                            (select city_id from customer where id = {selector}) as "gg" where status = true and c.id = gg.city_id """
            result = self.getData(table, fields, selector)
            fieldNames = ["id", "employee", "city_name",
                          "date_of_order", "customer", "product_name", "price", "status"]
            changeRes = []
            for item in result:
                cort = {}
                for index, element in enumerate(item):
                    cort[fieldNames[index]] = element
                changeRes.append(cort)
        else:
            changeRes = "Invalid loging!"
        return changeRes

    def login_self(self):
        return self.login_check(self.login, self.password, 'adm')


if __name__ == '__main__':
    admin1 = Admin('Admin', 'Admin')
    # orders = admin1.get_order_info()
    # print(orders)
    # data = [{
    #         # 'id': 8,
    #         'category_name': 'Rom'
    #         }]
    # put = admin1.add_product_category(data)
    # print(put)
    # id = admin1.getNextId('product_category')
    # print(id)
    # data = {
    #     'category_name': 'Water'
    # }
    # edit = admin1.edit_product_category(data, "category_name = 'Rom'")
    delete = admin1.delete_product_category('Water')
    print(delete)
