print(f'--------------- Running: {__name__} ---------------')

def func(file_name, namespace):
    print(f'\n\t---------- {file_name} ----------')
    for k, v in namespace.items():
        print(f'{k}: {v}')
    print(f'\t-------------------------------------\n')

func('module1 namespace', globals())

print(f'--------------- End of: {__name__} ---------------')


#_________________________________________________________________________________________________
# the __name__ attribute:

# whenever we execute this module directly, the __name__ attribute will be set to __main__.

# therefore, if we execute this code indirectly, for exemple, from inside another module, 
# the __name__ attribute value will be the file name itself. in this case, `module1`.

# we can see that, if we execute the `main.py` module, that module is loading and executing 
# this `module1` module object in there. therefore, the __name__ attribute value in there will 
# be set to "module1".


# it happens because whenever we import an module object, Python automatically loads and execute
# that module. by using the __name__ attribute, we can prevent that automatically execution.
# we can specify if we do want or not want and what to execute based on the __name__ attribute
# value.
# maybe we want to execute the module in certain way if we execute the module direclty. and
# maybe we dont want to run any code at all when we import some module.


#_________________________________________________________________________________________________

# --------------- Running: __main__ ---------------

#       ---------- module1 namespace ----------
# __name__: __main__
# __doc__: None
# __package__: None
# __loader__: <_frozen_importlib_external.SourceFileLoader object at 0x000002>
# __spec__: None
# __annotations__: {}
# __builtins__: <module 'builtins' (built-in)>
# __file__: module1.py
# __cached__: None
# func: <function func at 0x000001>
#        -------------------------------------

# --------------- End of: __main__ ----------------
