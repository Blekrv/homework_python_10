# Empoloyee interface


import psycopg2
from config import *
from connection import Connection


class Employee(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def login_self(self):
        return self.login_check(self.login, self.password, 'emp')

    def get_order_info(self, selector=''):
        if self.login_self():
            table = ('orders',)
            fields = ('*',)
            selector = ''
            result = self.getData(table, fields, selector)
            return result

    def add_pr_category(self, data):
        if self.login_self():
            table = 'product_category'
            result = self.postData(table, data)
            return result

    def edit_pr_category(self, data, selector):
        if self.login_self():
            table = 'product_category'
            result = self.updateData(table, data, selector)
            return result

    def delete_pr_category(self, selector):
        if self.login_self():
            table = 'product_category'
            selector = f"category_name = '{selector}'"
            result = self.deleteData(table, selector)
            return result

    def edit_self(self, data, selector):
        if self.login_self():
            table = 'employee'
            result = self.updateData(table, data, selector)
            return result
