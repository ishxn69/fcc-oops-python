from phone import Phone
from keyboard import Keyboard

item1 = Keyboard("ixgKeyboardPro", 500, 3)

item1.apply_discount()

# we get 350 as we had overriden the 'pay_rate' attribute in 
# Keyboard class initialization
print(item1.price) 


