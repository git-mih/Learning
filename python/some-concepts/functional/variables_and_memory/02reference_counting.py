# Reference counting
# we can keep track of these objects that are created in memory by tracking their memory addresses.

# we track how many other variables/names/symbols are poiting to that particular memory address, 
# to that same object essentially:
v1 = 10   # v1 ----> <'int' object at 0x01>            reference | count
#                                                        0x01        1

v2 = v1   # v1 ----> <'int' object at 0x01> <---- v2   reference | count
#                                                        0x01        2

del v2    # v1 ----> <'int' object at 0x01>            reference | count
#                                                        0x01        1

del v1    #                                            reference | count
#                                                        0x01        0

# once the referecen count of a particular object goes down to 0, Python memory manager will 
# destroy that object, and that corresponding memory address (0x01) will be avaiable again.


# we can check the references count of a particular object by using the sys module:
import sys
a = [1, 2, 3]
sys.getrefcount(a) # 2

# what happens is that, that function itself creates a extra reference to that list object.


# to get the refecence count without this drawback, we really should use the ctypes module:
import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

ref_count(id(a)) # 1

# once we destroy that list object:
a = None

# its memory space is avaiable to be used again:
ref_count(id(a)) # 4839208

# we should not directly deal with memory addresses in Python cause we cant relly on it. unless 
# we are trying to debug stuffs or figure out what is going on under the hood.
