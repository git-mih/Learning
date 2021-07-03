def Hanoi(number_of_disks, start_peg=1, end_peg=3):
	if number_of_disks:
		Hanoi(number_of_disks - 1, start_peg, 6 - start_peg - end_peg)
		print(f"move disk {number_of_disks} from peg {start_peg} to peg {end_peg}")
		Hanoi(number_of_disks - 1, 6 - start_peg - end_peg, end_peg)

print(Hanoi(4))