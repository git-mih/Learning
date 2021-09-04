# Namespaces:

# namespaces are just dict objects that contains symbols and its meaning essentially:
type(globals()) # <class 'dict'>


# creating a new symbol that will reference a function object in memory:
def func():
    a = 10
    return a

# that `func` symbol gets stored inside the local namespace (in this case, the module namespace).
# that symbol points to that function object somewhere in memory:
func  # <function __main__.func at 0x000001>


# Python knows where to find that function object in memory. it will look up for that symbol 
# inside the namespace (ddictionary) and get its reference. then we can access the object itself:
globals()   # {}..., 'func': <function func at 0x000001>}

# we can also recovery that function object reference ourselves:
globals()['func']   # <function __main__.func at 0x000001>
globals()['func']() # 10


# we can look at local namespaces as well:
def func():
    a = 10
    b = 20
    c = 'amy'
    print(locals())  

func()  # {'a': 10, 'b': 20, 'c': 'amy'}

#__________________________________________________________________________________________________
# Modules

# modules are object instances of the module type. they are just another type of objects.

# whenever we do an import, like:
import math, fractions
from typing import Collection

# we're essentially adding new symbols in the namespace that points to some object that were
# loaded and created in memory:
globals()
# {..., 'math': <module 'math' (built-in)>, 
#       'fractions': <module 'fractions' from \\lib\\fractions.py'>}

# in fact, we can access that module object by getting the symbol directly in the namespace:
globals()['math'] # <module 'math' (built-in) at 0x000001>

# we can look up their types:
type(math)       # <class 'module'>
type(fractions)  # <class 'module'>

# we could also change its variable name (symbol) and still having that module object reference:
xyz = fractions   # <module 'fractions' from '...\\Python39\\lib\\fractions.py' at 0x000003>
xyz is fractions  # True



# module object are basicly Singleton objects:
id(math)  # 0x000001

# it means that, if we try to load that module object in memory again, it wont reload:
import math
id(math)  # 0x000001

# in practice, when we import an module, it doesnt get loaded in the namespace itself. it will
# get loaded in the memory and its reference will be set into our global namespace.


# important to know that, the module object references are added into the system cache as well:
import sys

# we can see all modules that were loaded by looking into the system cache namespace.

# it is just a regular dictionary that contains symbols referencing the memory addres of where 
# the objects are located:
type(sys.modules) # <class 'dict'>
sys.modules       # {...}

# therefore, we could also get our objects by looking inside the system cache namespace:
sys.modules['math'] # <module 'math' (built-in)>

# and we can see that, in did they have the same memory address, either the system cache and
# our global namespace:
id(sys.modules['math']) # 0x000001
id(math)                # 0x000001

# what is happening essentially is that, while our code is running, the first time that we 
# import some module, it went ahead and load that module object in the memory. 
# then Python creates a reference to that object inside the sys.modules (system cache). 
# and after that, it adds that same symbol inside our global namespace.

# that is why we dont require to reload the module. if we try to reload an module again, Python
# will look inside the system cache to see if that module is already there. if is there, it just 
# return that same reference. 
# if doesnt, it loads the module object in memory, creates a new reference inside the system cache 
# and into the global namespace.

#______________________________________________________________________________________________________
# module object introspecting: 

import math

# we can look at the name of the module:
math.__name__  # math

# we can look up inside a dictionary that contains all the attributes that are avaiable inside 
# that module object:  (module object namespace)
math.__dict__  # {..., 'ceil': <built-in function ceil>, 'pi': 3.14159265, 'e': 2.71828182, ...}


# we can also get a list containing only the keys:
dir(math)  # [..., 'ceil', 'pi', 'e', ...]


# knowing that, we can create variable names that will reference these function objects:
ceil = math.__dict__['ceil'] # <built-in function ceil>

ceil(1.435)  # 2


# in fact, when Python encounter the `import..from` statement, it does that for us at runtime. 

# while our code is running, Python does all that steps of loading the module object in memory. 
# then it creates an symbol and its reference to that object inside the system cache. 
# but the major difference is that, it doesnt store the `math` symbol inside the global 
# namespace, it will store just the symbol that reference an particular object, in this case, 
# the <built-in function ceil>.

# once we do an `import..from`, we cant use math.ceil because we dont have that `math` symbol
# stored inside the global namespace. we only have the symbol `ceil` stored inside it.
# that is why we can just use `ceil` and get to that function object.

#___________________________________________________________________________________________________
# creating module objects:

from types import ModuleType

isinstance(math, ModuleType)      # True
isinstance(fractions, ModuleType) # True


# we can create our own module objects by using the ModuleType class:
m = ModuleType('my_module', 'this is a test module...')  # <module 'my_module'>

# that module object got its own namespace:
m.__dict__
# {'__name__': 'my_module', '__doc__': 'this is a test module...', '__package__': None, 
#  '__loader__': None, '__spec__': None}


# it doesnt have any functionality yet, but we could add some attributes on that object:
m.name = 'Fabio'
m.say_hello = lambda: f'hello {m.name}'
m.__dict__ # {..., 'name': 'Fabio', 'say_hello': <function <lambda> at 0x000001>}


# we cant use directly `say_hello` to access that function object. we dont have that symbol
# inside the global namespace: 
'say_hello' in globals() # False

# we would require to manually add that entry into the global namespace:
say_hello = m.say_hello

# now that is avaiable and we can call that function directly:
say_hello()  # hello Fabio

#___________________________________________________________________________________________________
# deep dive into the `import` statement:

# other languages like C, the modules gets compiled and linked ahead of time, before they run.
# in Python, everything happens during run-time. meaning that, we are going to load the 
# module objects during the program execution.

# in both cases, the system needs to know where those modules (files) are located. and for that, 
# Python uses a complex system of how to find the required modules (files). 
# that is the most complex part essentially, cause loading the module itself is quite 
# straightforward, easy to understand.


# the sys module has a few properties that defines where Python is going to look up for modules.
# either the built-in the standard modules, as well 3rd party and or own modules.

import sys

# we can see the Python installation path:
sys.prefix  # ...\Python\Python39

# using virtual environment:
sys.prefix  # ...\venv

# the compiled C binaries location:
sys.exec_prefix # ...\Python\Python39



# we can get the Path that Python go through to find modules:
sys.path

# whenever we import an module (file), Python needs to know where to find it. therefore, it is
# going to look in that Path essentially. 
# the Path is just a list containing all the directories that were registered. if it doesnt
# find the specified module in one of these paths, the import will fail.

# if you ever run into a problem where Python isnt able to import a module or a package, you 
# should check the path list to to make sure that, our module will be found by Python in there.

#_______________________________________________________________________________________________________
# this is how Python load an module:
#     - checks if the sys.modules (system cache) has already loaded the requested module. 
#       if so, it will just use that reference, otherwise:
#     - creates a new module object in memory, by using the types.ModuleType class;
#     - then it loads and execute the source code from the file;
#     - after that, it adds an new entry into the system cache by adding a symbol that will 
#       reference the module object namespace;
#     - finally, compiles and executes the source code.

# one thing that is really important to know is that, when a module is imported, that module is
# executed.


# NOTE: see 01exemple_A/main.py and test_module.py to proceed.

#_______________________________________________________________________________________________________
# loading modules manually: 

# we are going to mimick how Python load modules (files), how the `import` works essentially.
# for that, we require to use two built-in functions:
#     - the `compile` function which compiles the source (file text) into a code object;
#     - the `exec` function that is used to execute that code object. 

# we can optionally specify in which dictionary (namespace) we should store the global symbols.
# for that, we just require to specify it to the `exec` function which namespace that we want
# to use. in this case, we are going to store the global symbols inside our module namespace, 
# like Python does essentially.

# NOTE: see 01exemple_B directory.

#_______________________________________________________________________________________________________
# replacing the traditional `import` with functions:

# suppose that we are storing the name of some module that we want to import:
mod_name = 'collections'

# we cant import that by using the traditional `import` statement:
# import mod_name       ModuleNotFoundError: No module named 'mod_name'

# Python is essentially trying to find that `mod_name` module inside its look up Path.


# to actually be able to do that, we can use the importlib module. it is equivalent to the 
# regular import statement, but written in Python.
import importlib

# with that, we can perform that task of importing a module object based on its name basicly.
# the importlib have an import function, that will load the given module into the syste cache:
importlib.import_module(mod_name) # <module 'collections' from '...collections\\__init__.py'>
'collections' in sys.modules      # True


# but the thing is that, we doesnt have an direct reference to that module object. 
# it isnt added inside our global namespace:
# collections.defaultdict         NameError: name 'collections' is not defined


# it will just load the given module object and add an reference inside the system cache.

# it doesnt do anything else. it gets created in there, the sys.modules have that reference to
# the module object, but we dont have a handle to that module object inside our global namespace:
'collections' in globals()   # False



# at this point, to get that module object reference inside our namespace, we could get that
# reference manually from the sys module:
coll = sys.modules['collections'] # <module 'collections' from '...collections\\__init__.py'>
'collections' in globals()        # True

# we are essentially doing this:
import collections as coll


# or we could do everything in one shot:
math2 = importlib.import_module('math')  # <module 'math' (built-in)>
'math2' in globals()  # True

math2 is sys.modules['math']  # True


# this Python functional import function is writted in Python and it is equivalent to the 
# default `import` that was written in C. 
# we are doing the same thing by using the importlib.import_module essentially.

#_______________________________________________________________________________________________________
# Finders and Loaders (importer):

# the basic principle of how Python finds the modules inside our system.

# finders:
#     - objects that are responsible to find the requested module that we want to import.
#     - the finder objects are basicly functions. once Python see the `import` statement, it 
#       first goes and search for that module by using these finders.
#     - if the finder object doesnt know anything about that module, Python goes and ask to 
#       the next finder object that is avaiable.
#     - if the finder object knows where the requested module is, the finder object returns an
#       ModuleSpec object, which contains information about where Python can go and look for 
#       that particular module.
#     - once Python receives that ModuleSpec object, it go ahead and load that module.

# loaders:
#     - is the responsible to compile, execute and add the reference inside the system cache.
#       and potentially, add that symbol inside our global namespace, so we can be able to use 
#       that module object.

# finders + loaders is considered an importer.


# the finders returns an ModuleSpec object, and we can see that module specification by using 
# the __spec__ attribute that module objects provide:
math.__spec__  # ModuleSpec(name='math', 
#                           loader=<class '_frozen_importlib.BuiltinImporter'>, 
#                           origin='built-in')

# name:   name of the module
# loader: which loader Python should use to load and execute that particular module
# origin: the origin of where that module object is located.


# this ModuleSpec came back from some finder essentially. when we imported math, like:
import math

# Python asks if some of the finders know something about that module, one of the finders know,
# therefore, it returns to Python specifications to load and execute that module.


# the sys module provide a list containg all the finder objects avaiable:
sys.meta_path
# [<class '_frozen_importlib.BuiltinImporter'>,         1st
#  <class '_frozen_importlib.FrozenImporter'>,          2nd
#  <class '_frozen_importlib_external.PathFinder'>]     3rd

# these are the finders objects that, our Python will go and ask for the module specifications.
# we can see that our math module object was found by the BuitinImporter essentially:
math.__spec__.loader  # <class '_frozen_importlib.BuiltinImporter'>

# we can also get the ModuleSpec object of some module by using the importlib.util:
import importlib.util
importlib.util.find_spec('math') # ModuleSpec(name='math', 
#                                             loader=<class '_frozen_importlib.BuiltinImporter'>, 
#                                             origin='built-in')

#___________________________________________________________________________________________________
# writing our own finders and loaders:

# we could technically write our finders and loaders that can find and load our modules from a 
# database, or from an API directly. we dont have to import our modules from files only.


# if we try to import an custom module, like:
# import module1        ModuleNotFoundError: No module named 'module1'

# Python will essentially go trough that finder objects list:
sys.meta_path
# [<class '_frozen_importlib.BuiltinImporter'>,
#  <class '_frozen_importlib.FrozenImporter'>,
#  <class '_frozen_importlib_external.PathFinder'>]

# if neither of these finders is able to find our module1, Python raises that excpetion.



# lets create an module that is not inside the Python look up path. for that, lets add our 
# custom module inside the home directory:
import os

# getting the home directory:
external_path = os.environ.get('HOMEPATH')  # \\users\\username

# create our custom module `module1` inside the home directory:
file_abs_path = os.path.join(external_path, 'module1.py')
with open(file_abs_path, 'w') as f:
    f.write("print('running module1.py...')\n")
    f.write("city = 'Porto alegre'")

# tryng to get its ModuleSpec object:
importlib.util.find_spec('module1')  # None

# neither Python finder objects could find our custom module `module1`. they couldnt find that
# cause it isnt inside the Python path:
sys.path
# ['', # current directory.
#  'Python\\Python39\\python39.zip', 
#  'Python\\Python39\\DLLs', 
#  'Python\\Python39\\lib', 
#  'Python\\Python39', 
#  'Python39\\site-packages', 
#  'Python39\\site-packages\\win32', 
#  'Python39\\site-packages\\win32\\lib', 
#  'Python39\\site-packages\\Pythonwin', 
#  'Python\\Python39\\lib\\site-packages']

# that custom module `module1` is inside our home directory essentially, and Python doesnt have
# the home directory on its path.

# for that works, we just require to append the home directory inside that list:
sys.path.append(external_path)  # [..., \\users\\username]

# now that we have that, Python is able to get the ModuleSpec of our custom module: 
importlib.util.find_spec('module1')  
# ModuleSpec(name='module1', 
#            loader=<_frozen_importlib_external.SourceFileLoader object at 0x000001>, 
#            origin='C:\\users\\username\\module1.py')

# Python is able to get that module specification, therefore, it knows where to find and load:
import module1  # running module1.py...

# Python was able to get our module load that and execute it. it get stored isnide the system
# cache, as well inside our global namespace: 
sys.modules # {..., 'module1': <module 'module1' from 'C:\\users\\username\\module1.py'>}
globals()   # {..., 'module1': <module 'module1' from 'C:\\users\\username\\module1.py'>}

# with that module object reference, we can use its attributes:
module1.city    # Porto alegre
