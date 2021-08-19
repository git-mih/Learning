# Variables are memory references

# HEAP:

# memory:         [ ... | object1 |      | object2            |      |object3 |      | ... ]
# memory address:       0x01      0x02   0x03   0x04   0x05   0x06   0x07     0x08   0x99999       

# Python Memory Manager takes care about storing and retrieving object from the heap.


# whenever Python executes this statement, it will creates that int object in memory at some address:
my_var_1 = 10

# memory:         [ ... | 10   |      |      |      |      |      | ... ]
# memory address:       0x01   0x02   0x03   0x04   0x05   0x06   0x99999       

# we can find out the memory address referenced by a variable by using the id() function.
id(my_var_1)      # 238493584
hex(id(my_var_1)) # 0x01

# my_var_1 is referencing that object at 0x01, its value is equal to 0x01.

my_var_2 = 'Fabio' # its value is 0x04, and doesnt matter if its value overflows or not:
# memory:         [ ... | 10   |      |      |'Fabio'      |      |  ... ]
# memory address:       0x01   0x02   0x03   0x04   0x05   0x06   0x99999       

id(my_var_2)      # 459284702
hex(id(my_var_2)) # 0x04
