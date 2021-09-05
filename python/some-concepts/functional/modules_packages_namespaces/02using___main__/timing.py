# Using __main__:
"""Timing how long a snipped of code takes to run over multiple iterations..."""

print('Running timing.py file...')

from collections import namedtuple
from time import perf_counter
import argparse

Timing = namedtuple('Timing', 'repeats elapsed average')

def timeit(code, repeats=1):
    # compile the given code just once:
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()
    for _ in range(repeats):
        # executing the compiled code `n` times:
        exec(code)
    elapsed = perf_counter() - start
    average = elapsed / repeats
    return Timing(repeats, elapsed, average)
    #      Timing(repeats=50, elapsed=0.13, average=0.00263233600)

#__________________________________________________________________________________________________
# if we execute this module directly from the terminal, we can also get its functionality.

# for that, we will just require to pass the arguments trought the terminal:
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('code', type=str, help='code snippet that we want to time.')
    parser.add_argument('-r', '--repeats', type=int, default=1, help='n times to repeat.')
    args = parser.parse_args()

    print(f'timing: {args.code}')
    print(timeit(code=str(args.code), repeats=args.repeats))

    # executing `timing.py` module directly from terminal by using args:
    # Running timing.py file...
    # timing: [x**2 for x in range(10_000)]
    # Timing(repeats=50, elapsed=0.13, average=0.00263233600)
