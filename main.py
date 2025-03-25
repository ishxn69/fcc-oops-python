#we import a library to read CSV files.
import csv

class Item:
    pay_rate = 0.8
    all = [] 
    
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self) 
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate 
    
    #We use a class method (no self), since we have to instantiate objects from CSV
    #Since these are not part of the class, passing self doesn't make sense.
    
    #This is a decorator. They add new functionality (enhance/modify) 
    #to existing objects.
    @classmethod
    def instantiate_from_csv(cls): #notice class itself is passed as argument
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            #will count the floats that end with .0 as integers
            return num.is_integer()
        
        elif isinstance(num, int):
            return True
        
        else:
            return False
    
    def __repr__(self):
        return f'Item("{self.name}", {self.price}, {self.quantity})'

#After __repr__ method, output of Item.all is much more readable.

#Calling a class method:
#NOTE: I had gotten an error running this (error: item.get() returns None)
#the reason was that I had added spaces in csv file titles. There should be
#no space in csv files, just separate by commas.
Item.instantiate_from_csv()
print(Item.all)

#calling a static method
print('Is the provided number an integer?',Item.is_integer(7.0))