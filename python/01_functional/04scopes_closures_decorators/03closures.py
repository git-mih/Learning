# Closures

#_______________________________________________________________________________________________
# closures and free variables:

# remember that, inner functions can access the outer (nonlocal) variables:
def outer():
    x = 'Python'
    def inner():
        print(x)
    inner()
outer()
# when outer gets called, the inner function will get compiled and created. 
# during the compilation proccess, Python will pre-set that variable x as a nonlocal variable. 
# therefore, Python will look up for that variable x outside the inner scope.


# when the inner function get called, that nonlocal x is essentially referencing the outer
# scoped x. we call that nonlocal variable x a Free variable.

# when we consider the inner function, we are really looking at:
#   - the inne function object and the free variable x.

#  def outer():
#   _______________
#  /x = 'Python'   \
# |    def inner(): |
# |       print(x)  |--> free variable + the inner function object  -> Closure.
#  \_______________/
#    inner()       
# outer()

# the inner function do have its own local scope, but the free variable isnt stored inside
# it. it is living outside the inner function namespace scope essentially.


# when we have both, the inner function object and free variables binding together, we say
# that, the inner enclose its free variables, that is a closure.

#______________________________________________________________________________________________
# returning the inner function:

# what happens if, instead of calling the inner from inside the outer function, we return it?
def outer():
    x = 'Python' # \
    def inner(): #  ) closure:  <function object at 0x000001 + free variable (x)
        print(x) # /
    return inner # returning the closure object.

# we can assign that returned closure to a symbol:
f = outer()  # <function outer.<locals>.inner at 0x000001> 

# when we call that closure, we are essentially calling that inner function object, which have
# that free variable x:
f() # Python



# remember that, Python will evaluate and set that nonlocal variable x value only when we 
# call that inner function. but the thing is, we are calling it after the outer function 
# stops its execution. that nonlocal variable x was stored inside the outer scope essentially.
# how inner function still have that nonlocal x reference that was inside the outer scope?

# that closure retains/capture that free variable x. when we execute that outer function, is 
# the time where Python compiles that inner function object. at that time, Python notice that, 
# the inner function is enclosing that free variable, therefore, it do something with that.

#_______________________________________________________________________________________________
# Python cells and mlti-scoped variables:

# what happens when we have a variable that is inside two scopes? like, the variable inside
# the inner scope (nonlocal x) and the variable inside the enclosing function scope (x).

# we say that, that variable x has multiple scopes.
def outer():
    x = 'Python'
    def inner():
        print(x)
    return inner

# that symbol x is in two different scopes, but its value, its object being referenced is the 
# same string object essentially.

# that string object is being shared between these two scopes: outer and the closure.


# Python does that by creating an intermediary object, the cell object.
# and what the cell object does is just reference that string object essentially.

# under normal circunstances where we wont have that free variable x, we would not require
# an intermediary object to reference that. the variable itself would points directly, like:
def outer():
    def inner():
        x = 'Python' # points directly to the string object. doesnt require the cell object.
        print(x) 
    return inner

# however, when we have an closure (inner function + free variables), both variable names are
# referencing the same object, but they are between 2 different scopes, once the outer scope
# stop running, the inner scope need a mechanism to keep that nonlocal variable reference.

# Python realize that when we call the outer function and creates the inner function object.
# it realizes that, it should do some special thing with that. therefore, it creates that
# intermediary cell object to make both variable names reference the cell object, and the
# cell object keep the reference to the original object.

# essentially:
#     outer x  _______  
#                     |
#               <cell object> ---> <object at 0x1234>
#                  (0x0001)
#     inner x  _______|

# outer x = 0x0001
# inner x = 0x0001

# in fact, both variable names x reference the same cell object. whenever we request the value
# of that variable x, Python will essentially do a "double-hop" to get to the final object.


# same happens if we are setting the value, for exemple:
def outer():
    x = 'Python'
    def inner():
        nonlocal x
        x = 777
    return inner

# we are essentially changing the cell reference to point to another object:
#     outer x  _______  
#                     |             <'string' object at 0x0003> <<< GC
#               <cell object> --->  <'int' object at 0x0009>
#                  (0x0001)
#     inner x  _______|

# outer x = 0x0001
# inner x = 0x0001


# that should explain why the outer function when stops its execution, the closure keep track
# of where that nonlocal variable that was supposed to be out of scope is. 

# both variable names are referencing the cell object, once the outer function get out scope,
# the cell object doesnt get destroyed when the outer function stops.
# therefore, the inner function keeps referencing that:

#     outer x
#               <cell object> --->  <'int' object at 0x0009>
#                  (0x0001)
#     inner x  _______|

# inner x = 0x0001


#___________________________________________________________________________________________________
# we can think of closures as a function + an extended scope that contains free variables.

# the free variables value is the object that the cell object points to.
# every time the closure gets called and the free variable is referenced, Python look up for 
# the cell object, and the cell object reference to the object, its a "double-hop" essentially.

# it doesnt do that until we call the closure. when we create the inner function object by
# calling the outer function, we are essentially just creating the cell object and creating
# its pointers.

#___________________________________________________________________________________________________
# introspecting:

def outer():
    a = 10
    x = 'Python' # <'str' object at 0x000003>
    def inner():
        a = 777  # local variable.
        print(x)
    return inner

f = outer()  # <function outer.<locals>.inner at 0x000001>  closure.

# we can request all free variables that are avaiable inside the closure:
f.__code__.co_freevars  # ('x',)

# we can also get information about the cell object by using the __closure__ attribute:
f.__closure__  # (<cell at 0x000002: str object at 0x000003>,)

#___________________________________________________________________________________________________
# multiple instances of closures:

# every time that we run a function, a new local scope is created. if that function generates 
# an closure, a new closure is created every time as well:
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

# now we can create different instances of that closure (inner function + extended scope):
f1 = counter()  # <function counter.<locals>.inner at 0x000001>
f2 = counter()  # <function counter.<locals>.inner at 0x000005>

# a new cell object will be created for every time we call that closure:
f1.__closure__  # (<cell at 0x000002: int object at 0x000002>,)
f2.__closure__  # (<cell at 0x000006: int object at 0x000002>,) 
# both cells points to the same singleton object at this time.

f1() # 1
f1() # 2
f1() # 3
f1.__closure__  # (<cell at 0x000002: int object at 0x000012>,)

f2() # 1
f2.__closure__  # (<cell at 0x000006: int object at 0x00008>,) 

#___________________________________________________________________________________________________
# shared extended scopes:

# def outer():
#    _____________________
#   /   count = 0   --------> free variable -----> cell object ------>  <'int' object 0>
#  |   def inner1():      ||                            |
#  |       nonlocal count --> free variable ____________|
#  |       count += 1     ||                            |
#  |       return count   ||                            |
#  \_____________________/ |                            |
#    | def inner2():       |                            |
#    |     nonlocal count --> free variable ____________/
#    |     count += 1      |
#    |     return count    |
#    \_____________________/
#     return inner1, inner2

# both (inner1 and inner2) local scopes are sharing the same nonlocal variable (count) that 
# is inside the outer function scope.

def outer():
    count = 0
    def inner1():
        nonlocal count
        count +=1
        return count

    def inner2():
        nonlocal count
        count +=1
        return count
    return inner1, inner2

f1, f2 = outer() 
# f1 <function outer.<locals>.inner1 at 0x000001> 
# f2 <function outer.<locals>.inner2 at 0x000002>

# both closures are sharing the same cell object essentially:
f1.__closure__ # (<cell at 0x000007: int object at 0x000005>,)
f2.__closure__ # (<cell at 0x000007: int object at 0x000005>,)

# it means that, if we change the cell reference of f1, it will affect f2 as well:
f1() # 1
f1() # 2
f1() # 2

f1.__closure__ # (<cell at 0x000007: int object at 0x001234>,)
f2.__closure__ # (<cell at 0x000007: int object at 0x001234>,)
f2() # 4



# beware when defining function objects inside an iteration statement, for exemple:
l = []
for n in range(3):      
    l.append(lambda: n)  
    # defining a function object while iterating. defining closures, essentially.

# on each iteration, our lambda function expression is trying to access a variable name 
# that is out of its scope:
#       ___________________
#      / ,--------------------> free variable ----> cell obj ----> integer obj
# for | n in range(3):      |                         |
#     | l.append(lambda: n)---> free variable --------|
#      \___________________/

# we are essentially creating closures while iterating. the thing is that, all closures are
# sharing the same outer scope (variable name 'n' inside the for loop scope).

# first iteration:
# the nonlocal variable 'n' of the function is bound to the outer variable 'n' that is avaiable 
# inside the for loop scope. during the first iteration, Python creates that cell object and
# bind the nonlocal 'n' of the function + the variable 'n' created in the for loop.

# second and third iterations:
# another closure gets created, but the nonlocal variable 'n' of these second/third function 
# objects will be bound to the outer variable name 'n' that was defined in the for loop during 
# the first iteration.

# essentially, would be something like this:
# def for():
#     n = 0 
#     def iteration_1():
#         nonlocal n
#         n += 1       <cell object  --->  <integer object at 0x000>
#                        at 0x123>
#     def iteration_2():
#         nonlocal n                       <integer object at 0x000>  GC
#         n += 1       <cell object  --->  <integer object at 0x002>
#                        at 0x123>
#     def iteration_3():                   <integer object at 0x000>  GC
#         nonlocal n                       <integer object at 0x002>  GC
#         n += 1       <cell object  --->  <integer object at 0x006>
#                        at 0x123>

# in this example, we are creating 3 function objects, but they all share the same outer scope.
# they all are goin to share the same variable name that was defined in the loop.

# Python will make sure to bind them together through that cell object, but what happens
# is that, for each iteration, that cell object change its reference to another object.


# a new closure gets created for every iteration. it happens cause Python is just defining 
# these function objects, we are not evaluating their values. we will actually evaluate that
# variable 'n' when we call these function objects, but that time we call them, the cell
# object will be referencing the last 'n' value, which was 2 in our exemple.


# we got 3 different function objects appended on that list:
l # [<function <lambda> at 0x01>, <function <lambda> at 0x02>, <function <lambda> at 0x03>]

# but is important to know that, they will only be evaluated once we actually call them.
# once we call them, that outer variable 'n' (for loop 'n') will be evaluated:
l[0]() # 2

# by the time we actually call it, Python will then look up for the value that the cell object 
# is referencing. the loop stoped its execution, but that cell object still referencing that 
# outer variable 'n' (for loop'n') that was created.

# the cell object was changed its references over the iterations. so, the same will happen if 
# we call another function:
l[1]() # 2

# the variable name 'n' of the for loop was changed to 2 in the last iteration, that is why 
# all free variables 'n' are going to be evaluated to 2 as well:
l[2]() # 2



# what we could do instead, is capture the outer variable value when the function object gets 
# created. we cant wait to get that value only when the function gets evaluated.
l = []
for n in range(3):
    l.append(lambda i=n: i)
# we are setting a default value for `i` essentially. it means that, whenever that function
# object gets created, that variable name `i` will be pre-assigned with the current value 
# that the outer variable `n` is pointing to.

# in this case, we are not even creating closures, we are just creating regular functions:
l # [<function <lambda> at 0x1>, <function <lambda> at 0x2>, <function <lambda> at 0x3>]

# the value of `i` was pre-defined during that function object creation, it wont wait till
# we call the function to get that value anymore:
l[0].__defaults__ # (0,)
l[1].__defaults__ # (1,)
l[2].__defaults__ # (2,)

# we just call them, the value was defined during the function object creation:
l[0]()  # 0
l[1]()  # 1
l[2]()  # 2

# we can also override that pre-assigned default value:
l[0](i=5) # 5


#___________________________________________________________________________________________________
# nested closures:

# while compiling, Python pre-determines if variable names will be stored inside its own local
# scope or not.   during compilation, Python also create that cell object when required.

# therefore, when Python compile the incrementer outer function, it will determine that, 
# `n` must be a local variable to incrementer function, the outer function is also stored
# inside the incrementer function local namespace.

# but, `n` wasnt evaluated yet, it will actually happen when we call the incrementer function.
# by this time, Python actually evaluate the incrementer scope, it will see that, outer is
# going to have a local variable called `start`, will see that it also have another local
# variable called `current` and the inner function will be also stored inside its local scope.
# Python determine that once we actually call the incrementer function. during it, it also
# create the respective cell object to that inner function object, it know that, it is
# using the nonlocal keyword and require to create that cell object to hold that reference.
# it also create another cell object when it see that, the inner function is referencing the
# nonloval variable `n`, therefore, Python creates that cell object to reference it.
def incrementer(n):
    def outer(start):
        current = start 
        def inner():    
            nonlocal current
            current += n 
            return current

        return inner
    return outer

# representation of each namespace scope definition:
# incrementer:
#            n     ---> local  <_______________________________ 
#            outer ---> local:                                 \
#                         |                                 cell 0x2
#                       outer:                                  |
#                            start   ---> local,                |
#                            current ---> local, <______________|____
#                            inner   ---> local:                |    \
#                                           |                   | cell 0x1 
#                                         inner:                |     |
#                                              current ---> nonlocal (free variable) 
#                                                               |
#                                              n       ---> nonlocal (free variable)

# notice that, even though we are just referencing the outer scope `n` while creating the
# outer function object, Python still make that a free variable. 
# we are only required to use `nonlocal` keyword if we want to change the variable reference.


# creating the outer function + the extended scope containing the free variable `n`:
f = incrementer(2)     # <function incrementer.<locals>.outer at 0x1>
f.__closure__          # (<cell at 0x000001: int object at 0x000007>,) 
f.__code__.co_freevars # ('n',)


# when we call `f`, we are actually calling that outer function:
fn = f(0) # <function incrementer.<locals>.outer.<locals>.inner at 0x2>
fn.__closure__         # (<cell at 0x000002: int object at 0x000008>, -> inner cell object
#                         <cell at 0x000001: int object at 0x000007>) -> outer cell object.
fn.__code__.co_freevars # ('current', 'n')


# when we call `fn`, we are actually calling the inner function:
fn() # 2     current=0   +n (0+2)
fn() # 4     current=2   +n (2+2)
fn() # 6     current=4   +n (4+2)...

# essentially:
# incrementer -> outer(2) --> cell obj 0x1---> 2

# current     -> inner(0) --> cell obj 0x2---> int object 0

#                             cell obj 0x2---> int object 2
#                                              int object 0 GC

#                             cell obj 0x2---> int object 4
#                                              int object 2 GC
#                                              int object 0 GC

#                             cell obj 0x2---> int object 6
#                                              int object 4 GC
#                                              int object 2 GC
#                                              int object 0 GC
