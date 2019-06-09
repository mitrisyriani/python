# reads a file and parse all the 'From ' emails and prints them out

while True:
	try:
		fname = input("Enter file name: ")
		fh = open(fname)
		break
	except:
		print("Oops!  That was not a valid file name.  Try again")

counter = 0
for line in fh:
	line = line.rstrip()
	if line.startswith('From '):
		words = line.split()
		print(words[1])
		counter += 1

print("There were", counter, "lines in the file with From as the first word")