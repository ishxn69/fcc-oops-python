class Item:
    # added datatypes to the constructor attributes
    def __init__(self, name: str, price: float, quantity=0):
        #perform validation on the values received for attributes
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        #assigned values to self object
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

