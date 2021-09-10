# Variable re-assignement

# suppose we create this int object in memory:
a = 10     # 0x000001       a ----> <'int' object at 0x000001>

# now we re-asign its value:
a = 20     # 0x000006       a       <'int' object at 0x000001>  <---- GC
#                            \____> <'int' object at 0x000006>

# notice that, the memory address of `a` was changed. we are essentially creating a new object
# and changing the reference of `a` to that new object.

# creating another object and changing its reference to that particular new int object:
a = a + 10 # 0x000008       a       <'int' object at 0x000006>  <---- GC
#                            \____> <'int' object at 0x000008>

# we had not changed the internal state of the object at these addresses. we only created new
# objects and change its references.
