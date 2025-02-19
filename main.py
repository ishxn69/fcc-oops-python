class Item:
    pay_rate = 0.8 
    
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    #method to apply discount
    def apply_discount(self):
        #if we use Item.pay_rate, we won't be able to change pay_rate for each instance
        self.price = self.price * self.pay_rate 

item1 = Item('Phone', 100, 5)

item2 = Item('Laptop', 1000, 3)

item1.apply_discount()
print(item1.price) #80.0
item2.pay_rate = 0.7
item2.apply_discount() #here we change pay_rate of class level to instance level
print(item2.price) #700.0


