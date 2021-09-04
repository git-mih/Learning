# main.py

# this is how Python load an module:
#     - checks if the sys.modules (system cache) has already loaded the requested module. 
#       if so, it will just use that reference, otherwise:
#     - creates a new module object in memory, by using the types.ModuleType class;
#     - then it loads and execute the source code from the file;
#     - after that, it adds an new entry into the system cache by adding a symbol that will 
#       reference the module object namespace;
#     - finally, compiles and executes the source code.
#     - it also adds a symbol inside the global namespace that will reference that module object.

# one thing that is really important to know is that, when a module is imported, that module is
# executed.

#_______________________________________________________________________________________________________

print(f'\n=======================================================================')
print(f'\tRunning main.py - module name: {__name__}\n')

import module1  

print(f'\n=======================================================================')

# whenever Python reaches that import statement, it will execute the entire module essentially:
# =============================================================================================
#         Running main.py - module name: __main__

# --------------- Running: module1 ------------     # notice that, the __name__ attribute value
#                                                     isnt __main__ anymore. it happens cause we are 
#         ---------- module1 namespace ----------     executing that module indirectly.
# __name__: module1
# __doc__: None
# __package__:
# __loader__: <_frozen_importlib_external.SourceFileLoader object at 0x000002>
# __spec__: ModuleSpec(name='module1', 
#                      loader=<_frozen_importlib_external.SourceFileLoader object at 0x000002>, 
#                      origin='module1.py')
# __file__: ...\module1.py
# __cached__: ...\__pycache__\module1.cpython-39.pyc
# __builtins__: {...}
# func: <function func at 0x000001>     # we have that function object reference.
#         -------------------------------------
#
# --------------- End of: module1 ---------------
# =============================================================================================


# we got that symbol `module1` that points to that module object that was executed:
module1  # <module 'module1' from '...\test_module.py'>


# we have access to that function object that is inside the module object namespace:
globals()['module1'].__dict__['func'] # <function func at 0x000001>
module1.func                          # <function func at 0x000001>


# we can call that function to print the `main.py` module namespace:
module1.func('main namespace', globals())
#         ---------- main namespace ----------
# __name__: __main__                        # we are executing the `main.py` module directly. 
# __doc__: None                               the __name__ value will be set to __main__.
# __package__: None
# __loader__: <_frozen_importlib_external.SourceFileLoader object at 0x000002>
# __spec__: None
# __annotations__: {}
# __builtins__: <module 'builtins' (built-in)>
# __file__: ...\main.py
# __cached__: None
# module1: <module 'module1' from '...\module1.py'>
#         -------------------------------------


#___________________________________________________________________________________________________
# re-loading the same module object:

# if we try to import that module again, we cant expect that to get executed. it wont happen.

# Python will first see if that module object has already been loaded inside the system cache:
import sys
'module1' in sys.modules # True

# therefore, nothing will happen if we try to import that again:
import module1  


# we could try to remove that module object reference from inside our global namespace: 
del globals()['module1']

'module1' in globals()   # False

# but we essentially just just lost the reference that we had to that module object inside our 
# global namespace. so now, we cant access its attributes anymore:
# module1.func     NameError: name 'module1' is not defined


# and if we try to import that module again, we will basicly just create that symbol inside our 
# global namespace again to get a reference to that module object:
import module1
globals()  # {..., 'module1': <module 'module1' from '\module1.py'>}


# notice that, the module object doesnt get loaded again. it doesnt happen because its stored 
# inside the system cache essentially:
'module1' in sys.modules # True

# to be able to load and execute that module object again, we would have to delete the reference 
# that is inside the system cache to be able to load the module again:
del sys.modules['module1']

# now if we try to import, it will do all that steps of loading, references, symbols, etc:
import module1
# =============================================================================================
#         Running main.py - module name: __main__

# --------------- Running: module1 ------------     # notice that, the __name__ attribute value
#                                                     isnt __main__ anymore. it happens cause we are 
#         ---------- module1 namespace ----------     executing that module indirectly.
# __name__: module1
# __doc__: None
# __package__:
# __loader__: <_frozen_importlib_external.SourceFileLoader object at 0x000002>
# __spec__: ModuleSpec(name='module1', 
#                      loader=<_frozen_importlib_external.SourceFileLoader object at 0x000002>, 
#                      origin='module1.py')
# __file__: ...\module1.py
# __cached__: ...\__pycache__\module1.cpython-39.pyc
# __builtins__: {...}
# func: <function func at 0x000001>     # we have that function object reference.
#         -------------------------------------
#
# --------------- End of: module1 ---------------
# =============================================================================================


#___________________________________________________________________________________________________________
# to make the point, we can add a new entry inside the sys.modules (system cache) manually and
# import that. 
# in fact, if we load a function object instead a module object and import that, we will 
# immediately just returns that function object reference:
sys.modules['say_hello'] = lambda: 'hello world'

sys.modules  # {..., 'say_hello': <function <lambda> at 0x000001>}

# if we import that, we will essentially add a new symbol called `say_hello` inside our global
# namespace, and that symbol will will be a reference to that function object:
import say_hello

globals()    # {..., 'say_hello': <function <lambda> at 0x000001>}

# we can use that function directly now:
say_hello()  # hello world


# it is essentially showing to us that, when Python reaches that import statement, it will look
# inside the sys.modules (system cache). if that symbol is already been loaded, it just return
# that reference. if isnt, it loads the module object and add that inside the system cache and
# global namespace, so we can use that inside our module.
