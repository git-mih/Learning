# Variable equality

# we can think of variable equality in two fundamental ways.

# Memory Address: 
# variables are pointer essentially, and we may want to find out if two variables are pointing 
# to the same object, the same memory address.

# to compare memory addresses we use the identity operator 'is':
a = 10  # <'int' object at 0x000001>
b = 10  # <'int' object at 0x000001>
a is b  # True

# its negation:
a is not b  # False
not(a is b) # False

# dont count on it cause it may change:
a = 'hello' # <'str' object at 0x000001>
b = 'hello' # <'str' object at 0x000001>
a is b      # True


# Internal state:
# we may also want to just compare the internal state of the objects, its data essentially. 
# for exemple, comparing the content of two lists, they may not reside at the same memory address,
# but they may have the same content.

# to compare the internal sate/data of objects, we use the equality operator '==':
a = [1, 2, 3]   # <'list' object at 0x000001>
b = [1, 2, 3]   # <'list' object at 0x000007>   

a == b   # True

# its negation:
a != b   
not(a == b)


# the None object is an real object that is managed by Python as well. 
# it can be assigned to variables to indicate that it is "empty" and not set.

# furthermore, Python will share references when assigning variables to the None object:
a = None  # <'NoneType' object at 0x000001>
b = None  # <'NoneType' object at 0x000001>
c = None  # <'NoneType' object at 0x000001> 
