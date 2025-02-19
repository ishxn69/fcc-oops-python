class Item:
    pay_rate = 0.8
    all = [] # Empty list to store all items of class. 
    
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self) # This will store every instance inside the list. Keeps track of instances.
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate 
    
    # since we got a very user unfriendly output when we printed Item.all
    # we will now create a __repr__ method to make it's representation more readable.
    # we return the instances exactly like they are instantiated
    # as this is the best practice according to Python documentation
    '''
    Why is the above a best practice? Because it helps us create instances immediately by
    copying the items of __repr__ method output and pasting it into the python console.
    '''
    def __repr__(self):
        return f'Item("{self.name}", {self.price}, {self.quantity})'
    
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

#After __repr__ method, output of Item.all is much more readable.
print(Item.all)

