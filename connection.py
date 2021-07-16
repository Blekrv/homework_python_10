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


class Connection():

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
        fields = list(data[0].keys())
        fields.append('id')
        values = ''
        for row in data:
            # value = f"({','.join(row.values())}),"

            value = f"""({','.join(map(lambda item: f"'{item}'" ,row.values()))}, {next_id}),"""
            next_id += 1
            # for key in item:
            #     value += item[key]
            # value += '),'
            values += value

        insert_query = f"""INSERT INTO {table} ({','.join(fields)}) VALUES {values[:-1]};"""
        cursor.execute(insert_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return 'Insert done!'

    def deleteData(self, table, selector=''):
        connection, cursor = self.openDB()
        delete_query = f"""
            delete from {table} where {selector}
            """
        cursor.execute(delete_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return 'delete done!'

    def updateData(self, table, data: dict, selector: str):
        connection, cursor = self.openDB()
        set_items = ''
        for key in data:
            set_items += f"{key} = '{data[key]}',"
        update_query = f"""
            update {table} set {set_items[:-1]} where {selector}
            """
        cursor.execute(update_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return 'Update done!'

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

    def delete_product_category(self, selector):
        table = 'product_category'
        selector = f"category_name = '{selector}'"
        result = self.deleteData(self, table, selector)
        return result

    def delete_employee(self):
        pass

    def delete_customer(self):
        pass

    def edit_product(self):
        pass

    def edit_product_category(self, data, selector):
        table = 'product_category'

        result = self.updateData(table, data, selector)
        return result

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
