import threading
import time

# Each thread takes a turn running to achieve concurrency
# GIL - Global Interpreter Lock, takes care about it, allowing only one thread to hold 
#	control of the Python interpreter

def drink():
	time.sleep(2)
	print('you drank coffee')

def eat():
	time.sleep(5)
	print('you eat breakfast')

def study():
	time.sleep(8)
	print('you finished studying')

# 1. they are all running in the main thread, will takes 15 sec till it prints
print(threading.active_count()) # 1
print(threading.enumerate())    # [<_MainThread(MainThread, started 3212)>]

###########################################################################

def drink():
	time.sleep(2)
	print('you drank coffee')

def eat():
	time.sleep(5)
	print('you eat breakfast')

def study(subject):
	time.sleep(8)
	print(f'you finished studying {subject}')

# 2. creating multiple threads for each function.
x = threading.Thread(target=drink, args=())
x.start()

y = threading.Thread(target=eat, args=())
y.start()

z = threading.Thread(target=study, args=('maths',))
z.start()

# note: it will be printed before the functions stop executing, cause the
# 		main Thread dont stop executing if we dont wait by using .join()

print(threading.active_count()) 
print(threading.enumerate())
# 4 Threads
# [
# 	<_MainThread(MainThread, started 10624)>, 
# 	<Thread(Thread-1, started 5948)>, 
# 	<Thread(Thread-2, started 6224)>, 
# 	<Thread(Thread-3, started 12480)>
# ]

# you drank .. eat .. finished.  (main function ends up before the functions) 

###########################################################################

def drink():
	time.sleep(2)
	print('you drank coffee')

def eat():
	time.sleep(5)
	print('you eat breakfast')

def study(subject):
	time.sleep(8)
	print(f'you finished studying {subject}')

x = threading.Thread(target=drink, args=())
y = threading.Thread(target=eat, args=())
z = threading.Thread(target=study, args=('maths',))

x.start() # call the drink fn
y.start() # call the eat fn
z.start() # call the study fn

# now the Main thread will wait till x,y,z stop executing
x.join()
y.join()
z.join()

print(threading.active_count()) 
print(threading.enumerate())

# you drank coffee
# you eat breakfast
# you finished studying maths
# 1
# [<_MainThread(MainThread, started 11196)>]
