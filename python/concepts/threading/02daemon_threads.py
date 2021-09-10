import threading
import time

# Daemon threads are threads that runs in background, not important for program to run
#	that means, our program wont be waiting for deamon threads to stop his execution. 
#	It is different from normal threads which we cant stop our program if the thread dont stop running. 

def timer():
	count = 1
	while True:	
		time.sleep(1)
		print(f'\rlogged in for: {count}', end='')
		count += 1

x = threading.Thread(target=timer)
print(f'is daemon? {x.isDaemon()}') # False
x.start()

result = input('press enter to exit\n\n')
# We should exit the program after tipe enter. it wont happen because it isnt a daemon
# 	it will keep waiting forever till the thread stop executing and finally stop the program.

########################################################

def timer():
	count = 1
	while True:	
		time.sleep(1)
		print(f'\rlogged in for: {count}', end='')
		count += 1

x = threading.Thread(target=timer, daemon=True) # daemon set to True
print(f'is daemon? {x.isDaemon()}') # True
# we could also use x.setDaemon(True) before start the thread.
x.start()

result = input('press enter to exit\n\n')
# the program will stop running now whenever we press enter.
# 	the thread wont continue running once the Main thread stop executing.	
#	all daemons will be killed at this time.
