# garbage collection

# as we create objects in memory, Python keeps track of the number of references we have to them.
# but, no matter what the number of references is, as soon that the reference count go down to 0, 
# Python memory manager will reclaim that memory space.

# but sometimes it just dont work and we have to understand what circular referencees is.


# lets say that, we have a variable `my_var1` that points to an `object A`. 
# if `my_var1` goes away by referencing other object, then its reference count goes from 1 to 0 
# then Python memory manager will destroy that object and reclaim the memory space.

# the `object A` now has an object instance `my_var2` that points to another object `object B`.
# at this point, if we get rid of the reference `my_var1`, the reference count to the `object A`
# goes down to 0. therefore, `object A` will get destroyed, and once it gets destroyed, 
# `object B` reference count also go down to 0 and the `object B` gets destroyed as well.

# now lets suppose that `object B` also have an object instance `my_var3`, and `my_var3` is
# referencing `object A` back. that is a circular reference. `object A` reference count is 2.
# and if we try to get rid of `my_var1`, `object A` still have its reference `my_var3`.

# Python memory manager cant clean circular references, and that is where the GC comes in.
# the garbage collector will look and be able to identify circular references and clean then up.

# GC can be controlled programmatically by using the gc module where we can interact with it and 
# modify its behavior. the GC is turned on by default.

import gc
import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

# looking into the GC to know if given object exist inside GC or not:
def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) is id(object_id):
            return f'object exists...'
    return 'not found'

class A:
    def __init__(self):
        self.my_var2 = B()   # object instance of B

class B:
    def __init__(self):
        # self.my_var3 = A() # object instance of A
        # infinite recursion...
        pass

gc.disable()

my_var1 = A()   # object instance of A

my_var1                   # <__main__.A object at 0x000001>
my_var1.my_var2           # <__main__.B object at 0x000002>
# my_var1.my_var2.my_var3 # <__main__.A object at 0x000002>


# storing the memory addresses:
id_a = id(my_var1)         # 0x000001
id_b = id(my_var1.my_var2) # 0x000002

# reference counts:
ref_count(id_a)  # 2
ref_count(id_b)  # 1

# they exist inside the garbage collector?
object_by_id(id_a) # object exists...
object_by_id(id_b) # object exists...

# removing a reference of object A:
del my_var1

ref_count(id_a)  # 1
ref_count(id_b)  # 1

# they still exist inside the garbage collector?
object_by_id(id_a) # object exists...
object_by_id(id_b) # object exists...

# running the garbage collection manually to perform the clean up:
gc.collect()

# and now, they still exist inside the garbage collector?
object_by_id(id_a) # not found
object_by_id(id_b) # not found

# that object instances of A and B doesnt exist anymore, but its corresponding address where
# realocated:
ref_count(id_a)  # 3897341
ref_count(id_b)  # 3901284
