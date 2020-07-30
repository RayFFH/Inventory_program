
class Product:
    def __init__(self, name, ID, quantity, price):
        self.name = name
        self.ID = ID
        self.quantity = quantity
        self.price = price

    def getvalue(self):
            return self.price and self.quantity


class Inventory:
    def __init__(self, type_item):
        self.type_item = type_item
        self.product = []

    def add_product(self, product):
        self.product.append(product)


a1 = Product("whitebag",12046,25,14)
a2 = Product("Blackbag",12046,25,14)
a3 = Product("Brownbag",12047,24,16)
a4 = Product("whiteshirt",12046,25,14)
a5 = Product("Blackshirt",12046,25,14)
a6 = Product("Brownshirt",12047,24,16)
a7 = Product("whitetrousers",12046,25,14)
a8 = Product("Blactrousers",12046,25,14)
a9 = Product("Browntrousers",12047,24,16)

i = 1

while i == 1:
    ans = input("What bag do you want to order.bag, shirt or trousers?")
    if ans == "bag":
        a1 = Inventory("Bag")
        ans2 = input("What colour?")
        if ans2 == "white":
            Inventory.add_product(a1)
        elif ans2 == "black":
            Inventory.add_product(a2)
        elif ans2 == "brown":
            Inventory.add_product(a3)
    elif ans == "shirt":
        a2= Inventory("Shirt")
        ans2 = input("What colour?")
        if ans2 == "white":
            Inventory.add_product(a4)
        elif ans2 == "black":
            Inventory.add_product(a5)
        elif ans2 == "brown":
            Inventory.add_product(a6)
    elif ans== "trousers":
        a3 = Inventory("Trousers")
        ans2 = input("What colour?")
        if ans2 == "white":
            Inventory.add_product(a7)
        elif ans2 == "black":
            Inventory.add_product(a8)
        elif ans2 == "brown":
            Inventory.add_product(a9)

inventory1 = Inventory(Bag)