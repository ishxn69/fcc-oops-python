class Item:
    #these methods with __ are known as magic methods.
    #added a default value to quantity attribute
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        #no need to pass parameters externally now that we
        #declared these attributes in constructor.
        return self.price * self.quantity

item1 = Item('Phone', 100, 5)

item2 = Item('Laptop', 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

