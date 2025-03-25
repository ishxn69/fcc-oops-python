# we import the 'Item' and 'Phone' classes from item.py 
# and phone.py respectively
from item import Item

item1 = Item('Phone', 100)

# Below, we set name and print (Which is possible due
# to getter and setter functions that we created.)
# We do not need to specify __name, we can simply 
# use the variable name without access modifier.

# item1.name = 'AnotherItem' will return Exception as
# It's length is above 10 chars
item1.name = 'OtherItem' #this will work

#validation check will run before value is printed.
print(item1.name)