# Reads in a file and returns a sorted list of words with no duplications 

while True:
	try:
		fname = input("Enter file name: ")
		fh = open(fname)
		break
	except:
		print("Oops!  That was not a valid file name.  Try again")

fr = fh.read()
lst = list()
words = fr.split()
for i in words:
	if i not in lst:
		lst.append(i)
lst.sort()
print(lst)
