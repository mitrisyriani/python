# implements recursion algorithm of Tower Of Hanoi problem

# move n pieces from source to a destination  

# src, dst, aux are pegs
def tower_of_hanoi(n, src, dst, aux):
	if n <= 0:
		return
	tower_of_hanoi(n-1, src, aux ,dst)
	print(src, dst)
	tower_of_hanoi(n-1, aux, dst, src)
	
tower_of_hanoi(3, "A", "C", "B")