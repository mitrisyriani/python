# Reads in a file and returns a sorted list of words with no duplications 

while True:
	try:
		#fname = input("Enter file name: ")
		fname = "romeo.txt"
		fh = open(fname)
		break
	except:
		print("Oops!  That was not a valid file name.  Try again")

lst = list()
for line in fh:
	words = line.strip().split()
	for i in words:
		if i not in lst:
			lst.append(i)
print(sorted(lst))