# Python Builtin and standard types

# certain types that we use commonly in Python like: int, str, list, tuple, ...
# these are actually in the builtin module.
l = [1, 2, 3]
type(l)              # <class 'list'>
# the list data type lives in the builtin, that is why we can use it directly.
isinstance(l, list)  # True

# but not every type that we use in Python is actually part of the builtin module

# some types are not aviable directly in the builtins. 
# the object instances of the <class 'type'> are, we can create then inside our module.
# but the type that they are is not actually part of the builtins module. 

# for exemple functions. we can create functions inside our module. but his type
# isnt avaiable for us, like, the function itself is a object instance of some class.

# this class is not defined in the builtins module. functions, modules, generators, ...
# their classes are defined in the types module.


def f():
	pass

# when we print the type of some object, it will returns an string representation 
# of the object type.
type(f)       # '<class 'function'>'


import types
def f():
	pass

type(f) is types.FunctionType     # True
isinstance(f, types.FunctionType) # True

# FunctionType
# LambdaType
# MappingProxyType
# CellType
# GeneratorType
# MethodType
# ModuleType

# and many more...