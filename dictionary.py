'''
Write a program to read through the email.txt and figure out 
who has sent the greatest number of mail messages. The program looks 
for 'From ' lines and takes the second word of those lines as the person 
who sent the mail. The program creates a Python dictionary that maps the sender's 
mail address to a count of the number of times they appear in the file. After the 
dictionary is produced, the program reads through the dictionary using a maximum loop 
to find the most prolific committer.
'''
while True:
	try:
		fname = input("Enter file: ")
		fh = open(fname)
		break
	except:
		print("Oops!  That was not a valid file name.  Try again")


num = dict()

for line in fh:
	if "From " in line:
		words = line.split()
		num[words[1]] = num.get(words[1],0) + 1

bign = 0
bigw = ""

for word,count in num.items():
	if bign is None or count > bign:
		bign = count
		bigw = word

print(bigw, bign) 
