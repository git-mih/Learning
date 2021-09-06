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
# __loader__: <_frozen_importlib_external.SourceFileLoader>
# __spec__: ModuleSpec(name='module1', 
#                      loader=<_frozen_importlib_external.SourceFileLoader>, 
#                      origin='module1.py')
# __file__: ...\module1.py
# __cached__: ...\__pycache__\module1.cpython-39.pyc
# __builtins__: {...}
# func: <function func at 0x000001>
#         -------------------------------------
#
# --------------- End of: module1 ---------------
# =============================================================================================



# our global namespace now have a reference to that module:
globals()
# {...,
#   'module1': <module 'module1' from '...\test_module.py'>
# }


# accessing that function object that is inside the module object namespace:
module1.func                          # <function func at 0x000001>

# essentially:
globals()['module1'].__dict__['func'] # <function func at 0x000001>



# calling the function that will print the given module object namespace:
module1.func('main namespace', globals())

#         ---------- main namespace ----------
# __name__: __main__                        # we are executing the `main.py` module directly. 
# __doc__: None                               the __name__ value will be set to __main__.
# __package__: None
# __loader__: <_frozen_importlib_external.SourceFileLoader>
# __spec__: None
# __annotations__: {}
# __builtins__: <module 'builtins' (built-in)>
# __file__: ...\main.py
# __cached__: None
# module1: <module 'module1' from '...\module1.py'>
#         -------------------------------------


#___________________________________________________________________________________________________________
# Adding a new entry inside the system cache manually:
import sys

# if we load a function object instead of an module object and import that, we will just returns 
# that function object reference instead:
sys.modules['say_hello'] = lambda: 'hello world'

sys.modules
# {..., 
#   'say_hello': <function <lambda> at 0x000001>
# }


# if we import that, we will essentially add a new symbol called `say_hello` inside our global
# namespace, and that symbol will reference that function object:
import say_hello

globals()
# {..., 
#   'say_hello': <function <lambda> at 0x000001>
# }

say_hello()  # hello world


# it is essentially showing that, whenever Python import something, it will first look inside 
# the sys.modules (system cache), and if that symbol is already stored in there, it just adds
# a new symbol inside our global namespace that will reference the module object. 
# and if that symbol isnt already avaiable inside the system cache, Python load, execute and store 
# that module inside the system cache as well inside our global namespace.
