class Item:
    #added a class attribute
    pay_rate = 0.8 #20% discount to all items
    
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        #assigned values to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item('Phone', 100, 5)

item2 = Item('Laptop', 1000, 3)

print(Item.pay_rate)
print(item1.pay_rate)

# __dict__ is an inbuilt magic attribute that returns a dictionary of 
# all the attributes of a class for a class and all the attributes of
# an instance of a class for an instance of a class.
print(Item.__dict__)
print(item1.__dict__)

