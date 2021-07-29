# Empoloyee interface

class Employee:
    def __init__(self, firstname, lastname, dateofbirth, city, chief, login, password):
        self.firstname = firstname
        self.lastname = lastname
        self.dateofbirth = dateofbirth
        self.city = city
        self.chief = chief
        self.__login = login
        self.__password = password

    def edit_self_info(self):
        pass

    def change_order_status(self, order):
        pass
