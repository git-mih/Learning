# Global and local scopes

#_____________________________________________________________________________________________________
# scopes:

# when we assign an object to a variable like:
a = 10   # 0x000001
# that variable will be referencing some object in memory essentially.

# we usually say that, that variable is bound to the integer object 10.


# by using that symbol `a`, we can access that object in various parts of our code essentially. 
# but not everywhere.

# there might be places where that variable doesnt exists, or maybe it exist but means something
# else.

# there is this concept where that variable and its binding object will only "exist" on specific 
# parts of our code. the portion of code where that variable/binding object is defined, is called 
# Lexical scope of the variable or just Scope.

# one of the things that are associated with that scope is that, these binding objects are stored
# in somewhere. 

# that symbol `a` and its binding object do exist in some scope, but where it get stored?

# namespaces:
# we can think about it as a table that store that symbol `a` and its binding object `int 10`.


# is importanto to know that, each scope has its own namespace.

#______________________________________________________________________________________________________
# global scope:                                                     (module scope essentially)

# it spans into a single file only, so whenever we create a module in Python, his global scope 
# is the module itself.


# there is no really concept of a truly global scope that goes across all the modules in our 
# entire application, not in Python.

# but we do have something that is kinda truly global across all the modules, but that is the
# built-in scope. the scope where objects like, True, False, None, dict, print, etc...

# builtins and global variables can be used anywhere inside our module, even inside functions.

#______________________________________________________________________________________________________
# nested scopes: 

# global scopes are all nested inside the built-in scope:

#                                                            namespace representation:
# built-in                                                {'symbol':  <object at address>, ...}
#    |__ namespace: {'True': <builtin>, 'False': <builtin>, ...}                
#    |
#    |__ module1
#    |      |__ namespace: {'a': <int object at 0x0001, 'my_func': <function object at 0x00006}
#    |
#    |__ module2
#    .      |__ namespace: {'a': <int object at 0x0048, 'print': <function object at 0x12345}
#    .
#    .

# module scopes doesnt overlap other module scopes. each module will have its own namespace scope,
# each module will have its own global scope essentially.


# if we try to access some variable, it will first lokk inside its own namespace scope for that
# symbol. if it doesnt find it inside its own namespace, then Python will start looking back in 
# enclosing scopes namespaces. if it doesnt find anywhere, then Python raise an exception.

#______________________________________________________________________________________________________
# local scope:

# functions also have their own scopes. 
# when we create function objects, we can assign new variables inside the functions.

# these variable names will live inside the scope of that particular function object essentially.
def f():
    a = 10

# that integer object isnt created until we call that function.


# its really important to know that, when Python encounters a function definition while compiling,
# it will scan for any variable name that have values assigned to. 
# it will essentially look up everywhere in the function body while creating the function object.

# Python will consider any function parameter as a local variable during compilation and if some
# variable was not been explicitly specified as `global`, they will be also considered to be 
# local variables. 
# Python will be pre-determined to create and store these objects inside the function local scope 
# when the function gets called.


# it all happens during compilation. when Python encounter the function definition statement, 
# it makes some determinations where variable x is meant to be stored inside the local namespace, or 
# or wheter y should use the global namespace to store it, and so on.



# the local scope will get created only when the function gets called. therefore, every time the 
# function gets called, a new local scope will be created. 

# that make sense cause, when we call a function, we expect to pass different argument, different 
# objects for every call essentially.

# that is why recursion works. cause we are able to call the function from inside the function
# and everytime we're passing different values to it. everytime we call the function it gets its
# own local scope.


# parameters:
def f(a): 
# a: was pre-determined to be assigned into the function local namespace during the function 
# compilation.

# whenever we call the function, Python will create the function local scope and assign that
# variable to the given object: 
#   a = 'Fabio'
    print(a) # 'Fabio'

# the function local namespace scope will gets created only when the function object gets called:
f('Fabio')   # 'Fabio'


# variable assignments:
def f():
# for every assignment that Python encounter while creating the function object, they will 
# be stored in the local namespace scope as well: 
    a = 10


# reference counting and function scopes:  
def f():
    a = 10

f()
# when we run that function, the integer object 10 will be created in memory and its reference 
# will be incremented by one. 

# but as soon that function stop its execution, the local scope get destroyed and the reference 
# count for that integer object will be decreased by one.

# when it happens, we usually say that, the variable goes out of scope. 
# that variable `a` will no longer be avaiable once the function stop running. 

# that varialbe `a` will be avaiable only inside that function, outside the function, once the 
# function stop executing, `a` isnt avaiable, `a` is out of scope:
# print(a)   # NameError: name 'a' is not defined.

# once that function exit, the scope is gone. when the function stop executing, that scope is no 
# longer avaiable from outside.

#______________________________________________________________________________________________________
# Accessing the global scope from a local scope:

# when retrieving the value of a global variable from inside a function, Python automatically 
# look up for that variable inside its own local namespace first. 
# if it doesnt find, then it goes up in the chain searching inside enclosing scopes for that 
# particular variable:
#   local -> global -> builtins            (normal namespace lookup resolution)
#   local -> local -> global -> builtins   (nested functions exemple)


# but what if we want to modify a global variable reference from inside the function, like:
a = 10
def f():
    a = 777  # Python will interprets assignment operations to be considered local variables.

# when we call the function, that local scope will be created:
f() # 777

# the function local variable `a` was masking/shadowing the global `a` essentially:
a   # 10


# to actually be able to play with the global scope, we require to use the `global` keyword.
# by using that, we can tell Python that we want that variable to be scoped in the global scope.

# during compilation, Python will no longer pre-set that variable to be local, it will know that,
# it should store that variable inside the module namespace now:
a = 10    # 0x000001
def f():
    global a
# during compilation of the function object, Python will know that, it should scope this variable
# in the global (module) namespace.                            <'int' object at 0x000001>
    a = 777 # dealing with the global variable now:    a --->  <'int' object at 0x000004>

# creating and executing the function scope:
f() 

# we are essentially referencing to another integer object now:
a   # 100   0x000004


# variables that are just being referenced but doesnt get assigned anywhere in the function will 
# not be pre-determined to be local. 
# at run-time, Python will knows that it should look up for that variable inside enclosing scopes:
a = 10
def f():
    print(a)
# during compilation, Python will see in the entire function body that, the varialbe `a` is only
# being referenced by. therefore, Python will determine it as a non-local variable. 
# meaning that, during run-time it will goes and look up for that symbol `a` inside enclosing scopes.


#___________________________________________________________________________________________________________
# we can also create a global variable from inside the function local scope:

# trying to access a global variable that doesnt exists:
# print(x) # NameError: name 'x' is not defined.

def f():
    global x
    x = 999

# when we execute that function scope, that variable will be created in the global scope:
f()

# that global variable is avaiable in the module namespace:
'x' in globals() # True
x # 999

#___________________________________________________________________________________________________________
# caveats:
def f():
    # trying to access the pre-defined local variable `a` before it get assigned to an object:
    print(a)
    a = 10

f() # UnboundLocalError: local variable 'a' referenced before assignment.



# code blocks:
# variables works kinda the same way that when defining a variable using `var` in JavaScript:
for i in range(10):
    a = 42 
# that symbol isnt local to the block scope of the for loop only.

# it means that, the variable `a` and its bind object will be stored in the global scope:
'a' in globals() # True
a # 42
