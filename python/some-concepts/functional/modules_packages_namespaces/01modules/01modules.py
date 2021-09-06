# Namespaces:

# namespaces are just dictionary objects that contains symbols and its meaning essentially:
type(globals()) # <class 'dict'>


# creating a new symbol that will reference a function object in memory:
def func():
    a = 10
    return a

# that `func` symbol gets stored inside the local namespace (in this case, the module namespace).
# that symbol points to that function object somewhere in memory:
func  # <function __main__.func at 0x000001>


# Python knows where to find that function object in memory. it will look up for that symbol 
# inside the namespace (dictionary) and get its reference:
globals()   # {}..., 'func': <function func at 0x000001>}

# we can also recovery that function object reference ourselves:
globals()['func']   # <function __main__.func at 0x000001>
globals()['func']() # 10


# looking up at function local namespace:
def func():
    a = 10
    b = 20
    c = 'amy'
    locals()

func()  # {'a': 10, 'b': 20, 'c': 'amy'}

#__________________________________________________________________________________________________
# Modules

# modules are object instances of the module type. they are just another type of objects.


# whenever we do an import, like:
import math, fractions
from typing import Collection

# we're essentially adding new symbols in our global namespace that points to some object that 
# were loaded, executed and created in memory:
globals()
# {..., 
#   'math': <module 'math' (built-in)>, 
#   'fractions': <module 'fractions' from \\lib\\fractions.py'>
# }


# in fact, we can access that module object by getting that symbol directly in the namespace:
globals()['math'] # <module 'math' (built-in)>

# we can see that their data types are module objects essentially:
type(math)       # <class 'module'>
type(fractions)  # <class 'module'>


# if e change its symbol, we gonna still have that module object reference:
xyz = fractions   # <module 'fractions' from '...Python39\\lib\\fractions.py'>

#__________________________________________________________________________________________________
# module objects are basicly Singleton objects:

# it means that, if we try to load the same module object again, it wont reload:
import math  # id(math)  0x000001
import math  # id(math)  0x000001

#__________________________________________________________________________________________________
# System cache  (sys.modules):

# the system cache is where all modules get loaded, executed and stored before it get avaiable
# inside our global namespace. we can actually see all modules that were loaded by looking into 
# the system cache namespace.


# whenever we are importing a module, it doesnt get loaded in our global namespace at first.
# it will get loaded inside the system cache essentially. and a new entry will be added in there,
# and after that, we can get a reference to that module object into our global namespace.


# is important to know that, the reference to the module object is added into system cache first:
import sys, math
type(sys.modules) # <class 'dict'>
sys.modules
# {...,
#   'math': <module 'math' (built-in)>, ...
# }

# we can see that both symbols are references to the same module object:
id(globals()['math'])   # 0x000001
id(sys.modules['math']) # 0x000001


# getting a reference to the module object by using the system cache namespace:
math = sys.modules['math'] # <module 'math' (built-in)>

# that is equivalent to:
import math


# if we try to reload the same module again, Python will look inside the system cache to see if 
# that module is already in there. if is there, it just add a new reference to that module object
# inside our namespace:
del globals()['math']
'math' in globals()  # False

import math
'math' in globals()  # True

# if the system cache doesnt have the module object reference, it loads and execute that module, 
# creates a new reference to it inside the system cache and into the global namespace.

# that is why we dont require to reload the module. and is important to know that, even

#______________________________________________________________________________________________________
# module object introspecting: 

import math

# name of the module:
math.__name__  # math

# module namespace containing all attributes (properties and methods) of that module object:
math.__dict__  
# {..., 
#   'sqrt': <built-in function sqrt>,
#   'ceil': <built-in function ceil>,
#   'pi': 3.14159265,
#   'e': 2.71828182
# }

# list containing only the keys of the module namespace:
dir(math) # [..., 'sqrt', 'ceil', 'pi', 'e']


# with that, we can create labels that will reference these specific objects that are in there:
xyz = math.__dict__['ceil'] # <built-in function ceil>
xyz(1.435)  # 2

# equivalently:
from math import ceil as xyz

globals()
# {...,
#   'xyz': <built-in function ceil>
# }

# once we use `import..from`, we cant use math.ceil now. it happens because we dont have that 
# `math` symbol stored inside our global namespace anymore.

#___________________________________________________________________________________________________
# Creating module objects:

from types import ModuleType

isinstance(math, ModuleType)      # True
isinstance(fractions, ModuleType) # True


# creating our own custom module object by using the ModuleType class:
m = ModuleType('my_module', 'this is a test module...')  # <module 'my_module'>


# that module object have its own namespace:
m.__dict__
# {
#  '__name__': 'my_module', 
#  '__doc__': 'this is a test module...', 
#  '__package__': None, 
#  '__loader__': None, 
#  '__spec__': None
# }


# we can add attributes on that module object:
m.name = 'Fabio'
m.say_hello = lambda: f'hello {m.name}'
m.__dict__ 
# {..., 
#   'name': 'Fabio', 
#   'say_hello': <function <lambda> at 0x000001>
# }


# we cant access these attributes directly because we dont have any symbol that reference them
# inside our global namespace: 
globals()
# {...,
#   'm': <module 'my_module' from ...>
# }


# manually adding an entry into our global namespace to reference that module method:
say_hello = m.say_hello  

globals()
# {...,
#   'm': <module 'my_module' from ...>,
#   'say_hello': <function object at 0x0001>
# }

say_hello()  # hello Fabio

#___________________________________________________________________________________________________
# The `import` statement:

# other languages like C, modules get compiled and linked before they run.
# but in Python, the import is dinamicaly, happening during runtime. it means that, we are going 
# to load modules during the program execution.

# in both cases, the system needs to know where those modules (files) are located.
# for that, Python uses a complex system of how to find the required modules (files).
# that is the most complex part cause loading the module itself is quite easy to understand.


# the sys module has a few attributes that define where Python is going to look up for modules.
# either the built-in, standard library modules, as well 3rd party and or own modules:
import sys

# Python installation path:
sys.prefix  # ...\Python\Python39

# Python virtual environment as well:
sys.prefix  # ...\venv


# C binaries location:
sys.exec_prefix # ...\Python\Python39


# Path that Python look up for modules:
sys.path
# ['', 
#   '...Programs\\Python\\Python39\\python39.zip', 
#   '...Programs\\Python\\Python39\\DLLs', 
#   '...Programs\\Python\\Python39\\lib', 
#   '...Programs\\Python\\Python39', 
#   '...Roaming\\Python\\Python39\\site-packages', 
#   '...Roaming\\Python\\Python39\\site-packages\\win32', 
#   '...Roaming\\Python\\Python39\\site-packages\\win32\\lib', 
#   '...Roaming\\Python\\Python39\\site-packages\\Pythonwin', 
#   '...Programs\\Python\\Python39\\lib\\site-packages'
# ]

# whenever we import some module, Python needs to know where to find it.
# therefore, it is going to look in path list essentially.

# path is just a list containing all directories that were registered. if Python doesnt find 
# the requested module inside these paths, the import fails.

# if you ever run into a problem where Python isnt able to import a module or a package,
# you should really check the path list to make sure that your module will be found by Python.

#_______________________________________________________________________________________________________
# Module loading flow:

# NOTE: exemple1/main.py and module1.py

#_______________________________________________________________________________________________________
# Module Loading (manually): 

# we are going to mimick how Python load modules (files), how the `import` works essentially.
# for that, we require to use two built-in functions:
#     - the `compile` function which compiles the source (file text) into a code object;
#     - the `exec` function that is used to execute that code object. 

# we can optionally specify in which dictionary (namespace) we should store the global symbols.
# for that, we just require to specify it to the `exec` function which namespace that we want
# to use. in this case, we are going to store the global symbols inside our module namespace, 
# like Python does essentially.

# NOTE: exemple2/main.py

#_______________________________________________________________________________________________________
# importlib:

# we can replace the traditional Python import by using a functional approach with imporlib.


# suppose that we are storing inside a symbol the name of a module that we want to import:
mod_name = 'collections'

# we cant import that by using the traditional `import` statement:
# import mod_name       ModuleNotFoundError: No module named 'mod_name'

# Python is essentially trying to find that module inside its path list.


# to actually be able to do that, we should use importlib. 
# it is equivalent to the regular import statement, but is written in Python:
import importlib


# with importlib, we can import a module object just with its name essentially.
# it provides a import function that will load the given module into the syste cache for us:
importlib.import_module(mod_name)
sys.modules
# {...,
#   'collections': <module 'collections' from '...collections\\__init__.py'>  (package)
# }


# the thing is that, it doesnt provide a direct reference to that module object inside our 
# global namespace:
# collections.defaultdict   # NameError: name 'collections' is not defined

# it will load, execute and store a reference to that module object inside the system cache.
# doesnt do anything else:
'collections' in globals()  # False


# at this point, to get that module object reference inside our global namespace, we could 
# get a reference to that module manually from the system cache:
collections = sys.modules['collections']

globals()
# {..., 
#   'collections': <module 'collections' from '...collections\\__init__.py'>
# }

# equivalent:
import collections

#_______________________________________________________________________________________________________
# Finders and Loaders (importer):

# is the basic principle of how Python find and load modules inside our system.


# finders:
#     - are objects responsible to find the requested module that we want to import;
#     - once Python see the `import` statement, it goes and search for that module by using 
#       these finders objects. finders are functions that returns the module specification;
#     - if the 1st finder object cant find the requested module, Python ask to the next finder;
#     - if the finder object knows where the requested module is, it returns a ModuleSpec object, 
#       which contains information about where Python can go and how it can load that particular 
#       module;
#     - once Python receives that ModuleSpec object, it go ahead load and execute that module.
#
# loaders:
#     - responsible to compile, execute and add a entry inside the system cache that references 
#       an specific module.
#     - potentially add that same entry inside our global namespace, so we can access that module 
#       object directly.

# finders + loaders is considered an importer.


# __spec__:
# we can see module specifications of some module by using the module __spec__ attribute:
math.__spec__  
# ModuleSpec(name='math', 
#            loader=<class '_frozen_importlib.BuiltinImporter'>, 
#            origin='built-in')


# name:   name of the module;
# loader: which loader Python should use to load and execute that particular module;
# origin: the origin of where that module object is located.


# sys module provide a list containg all finder objects avaiable:
sys.meta_path
# [
#  <class '_frozen_importlib.BuiltinImporter'>,      1st
#  <class '_frozen_importlib.FrozenImporter'>,       2nd
#  <class '_frozen_importlib_external.PathFinder'>   3rd
# ]

# we can see that our math module object was found by the BuitinImporter essentially:
math.__spec__.loader  # <class '_frozen_importlib.BuiltinImporter'>


# we can also get the ModuleSpec object of some specific module by using the importlib:
import importlib.util
importlib.util.find_spec('math') 
# ModuleSpec(name='math', 
#            loader=<class '_frozen_importlib.BuiltinImporter'>, 
#            origin='built-in')



# we could technically write our finders and loaders that can find and load our modules from a 
# database, or from an API call essentially. we dont have to import our modules from files only.

#___________________________________________________________________________________________________
# Basic flow of finder objects:

# if we try to import an custom module, like:
# import module1    # ModuleNotFoundError: No module named 'module1'


# Python will essentially go trough that finder objects list:
sys.meta_path
# [
#  <class '_frozen_importlib.BuiltinImporter'>,
#  <class '_frozen_importlib.FrozenImporter'>,
#  <class '_frozen_importlib_external.PathFinder'>
# ]

# and these finder objects will essentially look up inside the sys.path:
sys.path
# [
#   '', 
#   '...Programs\\Python\\Python39\\python39.zip', 
#   '...Programs\\Python\\Python39\\DLLs', 
#   '...Programs\\Python\\Python39\\lib', 
#   '...Programs\\Python\\Python39', 
#   '...Roaming\\Python\\Python39\\site-packages', 
#   '...Roaming\\Python\\Python39\\site-packages\\win32', 
#   '...Roaming\\Python\\Python39\\site-packages\\win32\\lib', 
#   '...Roaming\\Python\\Python39\\site-packages\\Pythonwin', 
#   '...Programs\\Python\\Python39\\lib\\site-packages'
# ]

# neither finder is able to find our module1 cause our custom module isnt inside that path list.



# quick review on os.path:
import os 

# current directory:
os.path.abspath('')   # C:\...\modules_packages_namespaces\01modules
os.path.abspath('.')  # C:\...\modules_packages_namespaces\01modules

# going back single directory:
os.path.abspath('..') # C:\...\modules_packages_namespaces

# going back multiple directories:
os.path.abspath('../../..\\..') # C:\Users

#___________________________________________________________________________________________________
# Adding a new entry inside the Python look up path:

# getting the home directory:
external_path = os.environ.get('HOMEPATH')  # \\Users\\username


# create our custom module `module1` inside our home directory:
file_abs_path = os.path.join(external_path, 'module1.py')
with open(file_abs_path, 'w') as f:
    f.write("print('running module1.py...')\n")
    f.write("city = 'Porto alegre'")


# tryng to get its ModuleSpec object before adding our home directory inside the path list:
importlib.util.find_spec('module1')  # None


# appending the home directory inside the path list:
sys.path.append(external_path)
# [
#   '', 
#   '...Programs\\Python\\Python39\\python39.zip', 
#   '...Programs\\Python\\Python39\\DLLs', 
#   '...Programs\\Python\\Python39\\lib', 
#   '...Programs\\Python\\Python39', 
#   '...Roaming\\Python\\Python39\\site-packages', 
#   '...Roaming\\Python\\Python39\\site-packages\\win32', 
#   '...Roaming\\Python\\Python39\\site-packages\\win32\\lib', 
#   '...Roaming\\Python\\Python39\\site-packages\\Pythonwin', 
#   '...Programs\\Python\\Python39\\lib\\site-packages',
#   '...users\\username
# ]


# now that we have that, Python will be able to get the ModuleSpec of that module:
importlib.util.find_spec('module1')  
# ModuleSpec(name='module1', 
#            loader=<_frozen_importlib_external.SourceFileLoader>, 
#            origin='C:\\users\\username\\module1.py')


# Python will get that module specification, therefore, it knows how to load and execute that:
import module1  # running module1.py...

sys.modules
# {..., 
#   'module1': <module 'module1' from '...users\\username\\module1.py'>
# }

globals()
# {..., 
#   'module1': <module 'module1' from '...users\\username\\module1.py'>
# }


module1.city    # Porto alegre

#___________________________________________________________________________________________________
# import variants:

# the module is loaded and stored inside the system cache, no matter how we import that.
# the only thing that change depending the way that we import a module is what symbol will be 
# added inside our global namespace and what particular object that symbol will reference to.

# the reference can be either to the module object itself or just some attribute of that module 
# object. for exemple, an property or a function.


# regular import:
import math
globals()
# {..., 
#   'math': <module 'math' (built-in)>
# }

# equivalent:
math = sys.modules['math']


# import..as:
import math as xyz
globals()
# {..., 
#   'xyz':  <module 'math' (built-in)>
# }

# equivalent:
xyz = sys.modules['math']


# from..import:
from math import sqrt
globals()
# {..., 
#   'sqrt': <built-in function sqrt>
# }

# equivalent:
sqrt = sys.modules['math'].__dict__['sqrt']


# from..import..as:
from math import sqrt
globals()
# {..., 
#   'xyz': <built-in function sqrt>
# }

# equivalent:
xyz = sys.modules['math'].__dict__['sqrt']


# from..import..*:
from math import *
globals()
# {..., 
#   'sqrt': <built-in function sqrt>, 
#   'ceil': <built-in function ceil>, 
#   'pi': 3.141592
# }
