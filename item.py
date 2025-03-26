import csv

class Item:
    pay_rate = 0.8
    all = [] 
    
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        #set the name attribute as private
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        Item.all.append(self) 
    
    def calculate_total_price(self):
        return self.__price * self.quantity 

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
    
    #methods after we encapsulated the price attribute
    @property
    def price(self):
        return self.__price
    
    #we shifted the apply discount method from the bottomS
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    
    #method to apply increment.
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
    
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.__price}, {self.quantity})'
    
    # Now, these methods below do not actually work
    # Have used them as an example.
    def __connect(self, smpt_server):
        pass
    
    def __prepare_body(self):
        return f'''
        Hello User,
        We have {self.quantity} items of {self.name} at ${self.price} a piece!
        '''
    
    def __send(self):
        pass
    
    def send_email(self):
        self.connect('smtp.string')
        self.__prepare_body()
        self.__send()