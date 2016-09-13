class ContactList():

    


class Contact():

    all_contacts = []

    def __init__(self, name, email):

        self.name = name
        self.email = email
        self.__class__.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = []


class Supplier(Contact):

    all_contacts = []
    all_orders = {}

    def __init__(self, name, email):
        super().__init__(name, email)

    def order(self, string):
        self.__class__.all_orders.update({self.email: string})

x = Supplier(1, 2)
x.order("ddd")
print(Supplier.all_orders)
