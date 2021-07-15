# ADMIN INTERFACE
import psycopg2
from config import *
# connection = psycopg2.connect(
#     user=USER, password=PASSWORD, host=HOST, port=PORT, database='shop_db')
# cursor = connection.cursor()
# cursor.execute('SELECT VERSION()')

# print('Commit Success')
# if connection:
#     print('Connection closed')
#     cursor.close()
#     connection.close()


class Admin():
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @classmethod
    def openDB(cls):
        connection = psycopg2.connect(
            user=USER, password=PASSWORD, host=HOST, port=PORT, database='shop_db')
        cursor = connection.cursor()
        return connection, cursor

    @classmethod
    def closeDB(cls, connection, cursor):
        cursor.close()
        connection.close()

    def getData(self, table: tuple, fields: tuple, selector: str = ''):
        connection, cursor = self.openDB()
        select_query = f"""
            select {','.join(fields)} from {','.join(table)} {selector}
            """

        cursor.execute(select_query)
        connection.commit()
        result = cursor.fetchall()
        self.closeDB(connection, cursor)
        return result

    def postData(self, table, data: list):

        connection, cursor = self.openDB()
        next_id = self.getNextId(table)
        fields = data[0].keys()
        values = ''

        print(dict(fields))
        for row in data:
            # value = f"({','.join(row.values())}),"

            value = f"""({','.join(map(lambda item: f"'{item}'" ,row.values()))}),"""
            # for key in item:
            #     value += item[key]
            # value += '),'
            values += value

        insert_query = f"""INSERT INTO {table} ({','.join(fields)}) VALUES {values[:-1]};"""
        cursor.execute(insert_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return 'All done!'

    def updateData(self):
        pass

    def deleteData(self):
        pass

    def register_self(self):
        pass

    def add_product(self):
        pass

    def add_product_category(self, data):
        table = 'product_category'
        result = self.postData(table, data)
        return result

    def add_employee(self):
        pass

    def delete_product(self):
        pass

    def delete_product_category(self):
        pass

    def delete_employee(self):
        pass

    def delete_customer(self):
        pass

    def edit_product(self):
        pass

    def edit_product_category(self):
        pass

    def edit_employee(self):
        pass

    def get_order_info(self, selector=''):
        table = ('orders',)
        fields = ('*',)
        selector = ''
        result = self.getData(table, fields, selector='')
        return result

    def getNextId(self, table):
        table = (table,)
        fields = ('id',)
        result = self.getData(table, fields)[-1][0] + 1
        return result
    # def login(self):
    #     pass


if __name__ == '__main__':
    admin1 = Admin('Admin', 'Admin')
    # orders = admin1.get_order_info()
    # print(orders)
    # data = [{
    #         'id': 8,
    #         'category_name': 'Vine'
    #         }, {
    #         'id': 9,
    #         'category_name': 'Beer'
    #         }]
    # put = admin1.add_product_category(data)
    # print(put)
    id = admin1.getNextId('product_category')
    print(id)
