# Empoloyee interface

class Employee:
    def __init__(self, firstname, lastname, dateofbirth, city, chief, __login, __password):
        self.firstname = firstname
        self.lastname = lastname
        self.dateofbirth = dateofbirth
        self.city = city
        self.chief = chief
        self.__login = __login
        self.__password = __password

    def edit_self_info(self):
        pass

    def change_order_status(self, order):
        pass
