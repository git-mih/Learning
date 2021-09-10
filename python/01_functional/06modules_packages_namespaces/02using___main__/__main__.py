# Using __main__:

import sys
import timing  # loads and execute the timing.py module:
# Running timing.py file...

sys.modules  # {..., 'timing': <module 'timing' from '...timing.py'>}
globals()    # {..., 'timing': <module 'timing' from '...timing.py'>}


# code that we are going to compile and execute:
code = '[x**3 for x in range(10_000)]'

print(timing.timeit(code, 10))
# Timing(repeats=10, elapsed=0.0371894, average=0.003718939999)

#_________________________________________________________________________________________________
# another use case of the __main__ is that, we can execute Python modules by executing its 
# directory. for exemple, try to execute the directory that contains the __main__.py file:

# ~$ python .\02using___main__\

# Running timing.py file...
# Timing(repeats=10, elapsed=0.0371, average=0.003718939999)

# when we do that, Python will automatically look up for the __main__.py file and executes that.
