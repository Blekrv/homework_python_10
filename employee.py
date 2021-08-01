# Empoloyee interface


import psycopg2
from config import *
from connection import Connection


class Employee(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def get_order_info(self, selector=''):
        table = ('orders',)
        fields = ('*',)
        selector = ''
        result = self.getData(table, fields, selector)
        return result

    def add_pr_category(self, data):
        table = 'product_category'
        result = self.postData(table, data)
        return result

    def edit_pr_category(self, data, selector):
        table = 'product_category'
        result = self.updateData(table, data, selector)
        return result

    def delete_pr_category(self, selector):
        table = 'product_category'
        selector = f"category_name = '{selector}'"
        result = self.deleteData(table, selector)
        return result
