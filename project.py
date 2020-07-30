
class Product:
    def __init__(self, name, id, quantity, price):
        self.name = name
        self.id = id
        self.quantity = quantity
        self.price = price

    def getvalue(self):
        return self.price


class Inventory:
    def __init__(self, type_item):
        self.type_item = type_item
        self.products = []

    def add_product(self, product):
        self.products.append(product)


a1 = Product("whitebag", 12046, 25, 14)
a2 = Product("Blackbag",12046,25,14)
a3 = Product("Brownbag",12047,24,16)
a4 = Product("whiteshirt",12046,25,14)
a5 = Product("Blackshirt",12046,25,14)
a6 = Product("Brownshirt",12047,24,16)
a7 = Product("whitetrousers",12046,25,14)
a8 = Product("Blactrousers",12046,25,14)
a9 = Product("Browntrousers",12047,24,16)
product1 = Inventory("Bag")
product2 = Inventory("Shirt")
product3 = Inventory("Trousers")
i = 1

while i == 1:
    ans = input("What bag do you want to order.bag, shirt or trousers? or end?")
    if ans == "bag":
        ans2 = input("What colour?")
        if ans2 == "white":
            product1.add_product(a1)
        elif ans2 == "black":
            product1.add_product(a2)
        elif ans2 == "brown":
            product1.add_product(a3)
    elif ans == "shirt":
        ans2 = input("What colour?")
        if ans2 == "white":
            product2.add_product(a4)
        elif ans2 == "black":
            product2.add_product(a5)
        elif ans2 == "brown":
            product2.add_product(a6)
    elif ans == "trousers":
        ans2 = input("What colour?")
        if ans2 == "white":
            product3.add_product(a7)
        elif ans2 == "black":
            product3.add_product(a8)
        elif ans2 == "brown":
            product3.add_product(a9)
    elif ans == "end":
        print(product1.products[0].name)
