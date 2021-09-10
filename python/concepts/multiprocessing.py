from multiprocessing import Process, cpu_count
from time import perf_counter

# Running tasks in Parallel on different CPU cores bypassing the GIL used for threading.

def counter(n):
	count = 0
	while count < n:
		count += 1


def main():
	#_______________________________________________________ 1 core
	c1 = Process(target=counter, args=(100_000_000,))
	c1.start()

	c1.join()
	print(perf_counter()) # 7 seg ~

	#_______________________________________________________ 2 cores
	c1 = Process(target=counter, args=(50_000_000,))
	c1.start()

	c2 = Process(target=counter, args=(50_000_000,))
	c2.start()

	c1.join()
	c2.join()

	print(perf_counter()) # 4 seg ~

	#_______________________________________________________ 4 cores
	c1 = Process(target=counter, args=(25_000_000,))
	c1.start()

	c2 = Process(target=counter, args=(25_000_000,))
	c2.start()

	c3 = Process(target=counter, args=(25_000_000,))
	c3.start()

	c4 = Process(target=counter, args=(25_000_000,))
	c4.start()

	c1.join()
	c2.join()
	c3.join()
	c4.join()

	print(perf_counter()) # 3 seg ~



if __name__ == '__main__':
	main()
