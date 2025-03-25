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
    
    #We change the __repr__() method to include the name of the class
    #rather than hardcode it with string name, as otherwise it will print
    #'Item(name, price,quantity)' even for the child classes.
    #we do this using 'self.__class__.__name__'
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.price}, {self.quantity})'

#Example of Inheritance: The Phone class inherits from the Item class
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #The super method inherits all the attributes of the parent class
        #This includes the list all, hence we do not need to specify it again.
        super().__init__(name, price, quantity)
        assert broken_phones >=0, f"Broken phones {broken_phones} is not greater than or equal to zero!"
        
        self.broken_phones = broken_phones

phone1 = Phone('isgPhoneM12', 500, 6, 2)
# We can print Item.all and not 'Phone.all' and still see our item instance's data 
# added to the all list. This is because the all list is inherited from the parent 
# class. Also notice that it Prints Phone() instead of Item() since I had modified
# the __repr__() method.
print(Item.all)