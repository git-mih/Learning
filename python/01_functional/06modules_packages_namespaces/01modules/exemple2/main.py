# loading modules manually: 

# we are going to mimick how Python load modules (files), how the `import` works essentially.
# for that, we require to use two built-in functions:
#     - the `compile` function which compiles the source (file text) into a code object;
#     - the `exec` function that is used to execute that code object.

# we should specify which dictionary (namespace) we should store the global symbols.
# for that, we just require to specify it to the `exec` function the local namespace that we want.


# in this case, we are going to store the global symbols inside the module object namespace, 
# like Python does essentially.

#_________________________________________________________________________________________________

import os.path, types, sys

# getting the module (file) path:
module_relative_path = os.path.join('.', 'module1.py')
module_absolute_path = os.path.abspath(module_relative_path)


# reading the source code of our custom module `module1`:
with open(module_absolute_path, 'r') as f:
    source_code = f.read()


# creating the module object:
m = types.ModuleType('module1')   # <module 'module1'>

# specifying from where that module object is coming from:
m.__file__ = module_absolute_path # <module 'module1' from '...exemple2\\module1.py'>


globals()
# {..., 
#   'm': <module 'module1' from '...exemple2\\module1.py'>
# }


# storing a symbol and a reference to that module object inside the system cache:
sys.modules['module1'] = m  
# {..., 
#   <module 'module1' from '...exemple2\\module1.py'>
# }


# compiling the code that we loaded from that module:
code_object = compile(source_code, filename=module_absolute_path, mode='exec')
# <code object <module> at 0x000001, file "...module1.py", line 1>


# loading and executing that compiled code object:
exec(code_object, m.__dict__)    # Running module1.py...

# we essentially stored attributes inside that module object namespace after executing that
# compiled code object:
sys.modules['module1'].__dict__  
# {..., 
#   'name': 'Fabio', 
#   'hello': <function hello at 0x000001>
# }


# we can access that module object attributes:
m.hello()  # module1 says hello!
m.name     # Fabio



# our custom module is already stored inside the system cache, nothing will happen if we try to
# import that module again:
import module1



# even if we had another module, for exemple, if we are importing a `module2` and that `module2` 
# is importing the `module1` in there. that import will not load the `module1` again. 
# it doesnt happen cause we already had imported `import1`. therefore, it get stored inside the 
# system cache.
