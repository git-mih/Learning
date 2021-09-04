# main.py

# loading modules manually: 

# we are going to mimick how Python load modules (files), how the `import` works essentially.
# for that, we require to use two built-in functions:
#     - the `compile` function which compiles the source (file text) into a code object;
#     - the `exec` function that is used to execute that code object.

# we can optionally specify in which dictionary (namespace) we should store the global symbols.
# for that, we just require to specify it to the `exec` function which namespace that we want
# to use. in this case, we are going to store the global symbols inside the module object 
# namespace, like Python does essentially.

#_________________________________________________________________________________________________

import os.path, types, sys

# getting the module (file) path:
module_relative_path = os.path.join('.', 'module1.py')
module_absolute_path = os.path.abspath(module_relative_path)


# read source code from the module1.py file:
with open(module_absolute_path, 'r') as f:
    source_code = f.read()


# create the module object:
m = types.ModuleType('module1')   # <module 'module1'>

# specifying from where that module object is coming from:
m.__file__ = module_absolute_path # <module 'module1' from '...01exemple_B\\module1.py'>


# set an reference for that module object inside the system cache:
sys.modules['module1'] = m  # {..., <module 'module1' from '...01exemple_B\\module1.py'>}


# create a code object by compiling the source code (text) that we loaded from module1.py:
code_object = compile(source_code, filename=module_absolute_path, mode='exec')
# <code object <module> at 0x000001, file "...module1.py", line 1>


# loading and executing that compiled code object:
exec(code_object, m.__dict__)    # Running module1.py...

sys.modules['module1'].__dict__  # {..., 'name': 'Fabio', 'hello': <function hello at 0x000001>}



# that will essentially create the module object namespace, and will add an reference inside
# the global namespace to that module object:
globals()  # {..., 'm': <module 'module1' from '...module1.py'>}


# now that we have an reference to that module object, we can use its attributes:
m.hello()  # module1 says hello!
m.name     # Fabio

# we can try to import that module again, but it is already stored inside the system cache.
# nothing will happens:
import module1


# is important to know that, even if another module, for exemple, if we are importing another 
# module `module2` and that `module2` is importing the `module1` again in there. 
# that import will not load the `module1` object again. it wont happen cause we already have it 
# stored inside the system cache, Python will only returns that reference.
