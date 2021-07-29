from admin import Admin
from Registered_Customer import Customer
from pprint import pprint
import datetime
from custom import respprint
admin1 = Admin('Admin2', '1111')
admin1.register_self()


orders = admin1.get_order_info(category='status', selector=False)
print(orders)


# customer1 = Customer('Sania', '1234')
# customer1.register_self('Sania', 'Kuznetsov', 1)
# customer1.create_order([('Apple', 2), ('Meat', 2)])
# customer2 = Customer('rob', '1111')
# customer2.register_self('rob', 'gg', 2)
# customer2.login_self()

# print(customer2.first_name)
