import csv

class Item:
    pay_rate = 0.8
    all = [] 
    
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        #set the name attribute as private
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self) 
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate 

    @classmethod
    def instantiate_from_csv(cls): 
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
            return num.is_integer()
        
        elif isinstance(num, int):
            return True
        
        else:
            return False
    
    #This is the getter function for name object
    @property
    def name(self):
        # Property decorator = Read-only attribute 
        return self.__name
    
    #This is the setter function for name object
    @name.setter
    def name(self, value):
        #The setter function is called whenever the value of the name object is changed
        #We can add various lines of code that execute before the actual change takes place
        #This can be utilized to add validation checks, print statements, etc.
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
    
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.price}, {self.quantity})'