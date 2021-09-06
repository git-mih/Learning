# Packages

# Packages are essentially just modules. but a module isnt necessaraly an package. 

# we can think about a package as a specialized module that contains other modules. 
# but a package can also contains packages as well, we call them sub-packages.

# we can inspect if a module is a package or not, by looking at the __path__ attribute.
# modules that isnt a package, doesnt have the __path__ attribute. packages in the other hand,
# have the __path__ attribute defined. 
# its value is the absolute path where the package (module) is located.

#__________________________________________________________________________________________________
# Packages and file systems:

# we have finder and loader objects, therefore, modules doesnt have to be inside a file system. 
# by the same token, packages doest have to be a entity of a file as well.


# packages represent a hierarchy of modules and sub-packages: 
#  pack1
#    |__ module1.py <<
#    |__ module2.py
#    |
#    |__sub_package1
#    |       |__ module1.py 
#    |       |__ module2.py
#    |
#    |__sub_package2       
#    |       |__ utils
#    |       |     |__ module1.py <<
#            |
#            |__ module1.py

# we can represent that hierarchy by using dot notation, for exemple:
# pack1.module1
# pack1.sub_package2.utils.module1

# the dotted notations just indicates the path hierarchy of a module/package.

#__________________________________________________________________________________________________
# importing nested packages:

# if we have an import statement such as:
# import pack1.sub_package1.module1

# the import system will perform the following steps:
#     - first, it is going to import the package1 module, cause it cant import the remaining modules
#       without importing the pack1. the pack1 package have the reference to that sub_package1:
# import pack1
# system cache --> {'pack1': <module 'pack1' from ...>}
#
#     - after that, Python loads the sub_package1 which have a reference to the module that we
#       want to import:
# import pack1.sub_package1
# system cache --> {'pack1':              <module 'pack1' from ...>,
#                   'pack1.sub_package1': <module 'pack1.sub_package1> from ...}
#
#     - finally, it imports the requested module `module1`:
# import pack1.sub_package1.module1
# system cache --> {'pack1':                     <module 'pack1' from ...>,
#                  'pack1.sub_package1':         <module 'pack1.sub_package1> from ...,
#                  'pack1.sub_package1.module1': <module 'pack1.sub_package1.module1> from ...}

# the system cache (sys.modules) will contain entries for every module that get loaded.


# the thing is that, our global namespace will only contains a single entry, the reference to 
# the pack1 module:
# globals() ----> {'pack1': <module 'pack1' from ...}

#__________________________________________________________________________________________________
# File system based packages:

# although modules and packages can be far more generic than file system entities, it get tricky.
# gonna stick with the traditional file system based modules/packages.


# by using a file based system, we require to use directories to represent packages. 
# therefore, the directory name will represent the package name.
# just remember that, a package is simply a module that contain other modules or sub-packages.

# the thing is that, directories cannot contain code, so where does the code go for the package?
# since packages is a module essentially? __init__.py file.

# the package (module) code goes inside an special Python file called __init__.py. 
# it means that, when we have a package, we also have this __init__.py file, its mandatory that, 
# to that module be considered as a package, it must contain the __init__.py file in there.

#__________________________________________________________________________________________________
# __init__.py:

# that file tells Python that, that directory is actually a package, and not an standard directory.


# Python package import flow:
# src/
#    pack1/
#       |__ __init__.py
#       |__ module2.py


# when we do an import of that `pack1` package:
# import pack1

# its code will be inside that __init__.py file. therefore, that code get loaded, executed and
# cached inside the system cache (sys.modules) with a key of `pack1` and the value will be a 
# reference to the module object. 
# that symbol `pack1` will also be added to our namespace by referencing that module object.

# __path__:
# the only difference is that, it now has the __path__ attribute defined. regular modules dont.
# the value inside that __path__ attribute will be the absolute path of that directory.

# __file__:
# an package also have the __file__ attribute defined. its value will be the absolute path to 
# the __init__.py file. its the location from where the code of that module (package) came from.

# __package__:
# if the module is located in the root of our application, its value is just an empty string.
# but if the module is inside a package, its value is the package name essentially. like:
# import module
# module.__package__   # ''

# import pack1.module
# pack1.module.__package__  # pack1

# import pack1.sub_pack.module
# pack1.module.sub_pack.__package__  # pack1.sub_pack

#_________________________________________________________________________________________________
# NOTE: see packages/ directory and its exemple.txt file:
