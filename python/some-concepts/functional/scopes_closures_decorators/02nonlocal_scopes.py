# Nonlocal scope

# the local scope and the nonlocal scope are related, but they are a little different. 
# specially when we start defining nested inner functions.

# we can define function inside another function, like:
def outer_func():
    x = 'hello'
    def inner_func():
        print(x)
# its important to know that, the inner function local scope gets created only when we call and 
# executes the function itself:
    inner_func()

# when we call outer_func, the inner_func object will just be compiled and created.
# Python will create the outer local scope and add `x` and `inner_func` inside its namespace:
outer_func()  # hello

# when the inner_func gets compiled (when the outer function is called essentially), 
# Python make the determination that, the variable `x` will not be local in this case, there is 
# no assignments inside the inner_func. 
# therefore, when we runs the inner function, Python will search in the enclosing (outer_func) scope.

# essentially:  inner-local -> outer-local

#__________________________________________________________________________________________________________
# namespace look up resolution:
# Python will start looking for variable names from the inner local scope, if it doesnt find the
# variable name that its looking for, it goes back and look up in enclosing scopes, which is the
# outer local scope, if doesnt find, it goes and look back to the enclosing scope (global):

# essentially: inner-local -> outer-local -> module -> builtin


# both inner and outer functions have access to the global and builtin scopes:
a = 10
def outer_func():
    def inner_func():
        print(a, True)
    inner_func()

outer_func() # (10, True)


# there is a difference between the local scope and the global scope. 
# for exemple, if we have an variable being referenced inside the inner local scope that doesnt 
# exist inside its scope, Python will look in the outer scope for it. 

# the difference is that, in some cases it will continue to looking up inside the global scope, 
# and other cases it just stops when reaching the outer scope. it will happen only when we 
# excplicitly tell Python that we are working with a `nonlocal` variable.

#________________________________________________________________________________________________________
# modifying global variables from inside an inner function scope:

# we saw how we can use the `global` in order to modify a global variable within a nested scope:
a = 10
def outer_func():
    global a
    a = 777

# we can do the same thing from inside a inner function scope, it doesnt matter:
a = 10
def outer_func():
    def inner_func():
        global a
        a = 999
    inner_func()

outer_func()
a  # 999

#_________________________________________________________________________________________________________
# modifying nonlocal variables:

# we saw how variable assignment works during the function object creation:
def outer_func():
    x = 10
    def inner_func():
        x = 777
        # we are essentially just masking/shadowing the outer variable `x`.
        print(x) # 777
    inner_func()
    # at this point, the inner_func local scope was gone.
    print(x)     # 10   

outer_func()


# but we can modify variables that were defined in the outer nonlocal scopes. we just have to
# explicitly tell Python that we are going to work with a nonlocal variable.

# we can do that by using the `nonlocal` keyword:
def outer_func():
    x = 10 # object integer 10 will be gone.
    def inner_func():
        nonlocal x
        # during compilation of inner_func, Python will determine that, the variable `x` should
        # be scoped inside the outer scope.
        x = 777
    inner_func()
    print(x)  # 777
outer_func()

#_____________________________________________________________________________________________________
# nonlocal variables:

# whenever Python is told that, a variable is nonlocal, it will automatically look for that variable
# inside the enclosing local scope chain until it find the specified variable name:
def outer_func():
    a = 10 # first encountered.
    def inner_func():
        nonlocal a
        print(a) # 10
    inner_func()

outer_func() # 10

# we can also have more levels of nesting:
def outer_func():
    a = 10
    def inner_func():
        a = 777 # first encountered.
        def inner2_func():
            nonlocal a 
            print(a) # 777  
        inner2_func()
    inner_func()
outer_func()

# we can even chain nonlocal variables to keep going back to enclosing local scopes:
def outer_func():
    a = 10
    def inner_func():
        nonlocal a
        a = 999 # first encountered.
        def inner2_func():
            nonlocal a 
            print(a) # 999
        inner2_func()
    inner_func()
    print(a) # 999
outer_func() 

# but beware, it will only look inside the local scopes. it will not look in the global scope if
# we are using the nonlocal keyword. it means that, if neither nonlocal scopes have the specified
# variable defined on their namespaces, Python will not try to look up for it inside the globals:
a = 10
def outer_func():
    def inner_func():
        # nonlocal a
        pass
    inner_func()
outer_func()    # SyntaxError: no binding for nonlocal 'a' found
