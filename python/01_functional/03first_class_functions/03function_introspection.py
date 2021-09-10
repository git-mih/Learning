# Function introspection

# in general, introspection is simply the act of analize our code by using code. for exemple,
# we can use code to look at the code that we've writen, some information about a particular
# object, function, class, etc.


# remember that, function are first-class objects. they have attributes (properties and methods).
# we saw __doc__, __annotations__, but we can also attach our own attributes to it:
def f(a, b):
    return a + b

f.category = 'math'

# we can then return that:
f.category  # math


# we have a built-in function that, given an object, returns an list containing all valid attributes 
# that are avaiable in that particular object:
dir(f) # [..., __doc__, __annotations__, 'category']

# different of the __dict__  method, which returns the object namespace (dictionary) essentially:
f.__dict__ # {'category': 'math'}


# function attributes:
def my_func(a, b=2, c=3, *, kw1, kw2=2):
    name = 'Fabio'
    age = 26
    get_lang = lambda: 'python'

my_func.__name__       # my_func    is just the name of the function.
my_func.__defaults__   # (2, 3)     return a tuple that contains all default values.
my_func.__kwdefaults__ # {'kw2': 2} return a dict containing all keyword-only default arguments.


# there is the __code__ attribute as well:
my_func.__code__  # <code object my_func at 0x000001, ...>

# it returns a code object instance that have various properties like:
my_func.__code__.co_varnames # ('a', 'b', 'c', 'kw1', 'kw2', 'name', 'age', 'get_lang')
# return a tuple containing all parameter names, followed by local variable names.

my_func.__code__.co_argcount # 3  only positional and keyword arguments gets included.


#________________________________________________________________________________________________________
# inspect module:

import inspect

# objects have attributes, and attributes are essentially objects bounded to another objects.
# but when we have an attribute that is callable, we call it a Method:
class C:
    def f(self):
    # the function object `f` is an callable attribute that will be bound to instances of `C`.
        pass

C.f   # <function C.f at 0x000002>

obj = C()  # <__main__.C object at 0x000001>
obj.f # <bound method C.f of <__main__.C object at 0x000003>>

# we can inspect to see if given object is a function or a method:
inspect.ismethod(obj.f)   # True
inspect.isfunction(obj.f) # False

# isroutine will basicly look if its a function or a method:
inspect.isroutine(obj.f)  # True
inspect.isroutine(C.f)    # True


# by using code, we can also get the source code of some functions/methods, class and more:
inspect.getsource(C)
# class C:
#     def f(self):
#         pass

# we can find out the module where our function/method, class, was created:
inspect.getmodule(C)     # <module '__main__' from '...03function_introspection.py'>
inspect.getmodule(print) # <module 'builtins' (built-in)>


#___________________________________________________________________________________________________
# callable signatures:

def f(a: str,
      b: int = 10,
      *args: 'additional positional arguments',
      kw1: '1st keyword-only argument',
      kw2: '2nd keyword-only argument' = 20,
      **kwargs: 'additional keyword-only arguments') -> str:
      """docstring explaining something..."""
      pass

# we can get the signature of any callable object:
type(inspect.signature(f))  # <class 'inspect.Signature'>

# that signature object instance contains some attributes, in specific the `parameters`:
type(inspect.signature(f).parameters) # <class 'mappingproxy'>

# it essentially returns an dictionary object where the: 
#   keys: are the parameter names.
#   values: is an object with attributes such as `name`, `default`, `annotation`, `kind`:
inspect.signature(f).parameters.values()
# odict_values([<Parameter "a: str">, 
#               <Parameter "b: int = 10">, 
#               <Parameter "*args: 'additional positional arguments'">, 
#               <Parameter "kw1: '1st keyword-only argument'">, 
#               <Parameter "kw2: '2nd keyword-only argument' = 20">, 
#               <Parameter "**kwargs: 'additional keyword-only arguments'">])

# iterating through that dictionary view:
for param in inspect.signature(f).parameters.values():
    print(f'name: {param.name}')
    print(f'  default: {param.default}')
    print(f'  annotation: {param.annotation}')
    print(f'  kind: {param.kind}')

# name: a
#   default: <class 'inspect._empty'>
#   annotation: <class 'str'>
#   kind: POSITIONAL_OR_KEYWORD

# name: b
#   default: 10
#   annotation: <class 'int'>
#   kind: POSITIONAL_OR_KEYWORD

# name: args
#   default: <class 'inspect._empty'>
#   annotation: additional positional arguments
#   kind: VAR_POSITIONAL

# name: kw1
#   default: <class 'inspect._empty'>
#   annotation: 1st keyword-only argument
#   kind: KEYWORD_ONLY

# name: kw2
#   default: 20
#   annotation: 2nd keyword-only argument
#   kind: KEYWORD_ONLY

# name: kwargs
#   default: <class 'inspect._empty'>
#   annotation: additional keyword-only arguments
#   kind: VAR_KEYWORD

# we also have the POSITIONAL_ONLY kind, where is defined by using /:
for param in inspect.signature(divmod).parameters.values():
    print(f'parameter name: {param.name}  kind: {param.kind}')
# parameter name: x  kind: POSITIONAL_ONLY
# parameter name: y  kind: POSITIONAL_ONLY
