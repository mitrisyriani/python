# The program will prompt for a URL, read the XML data 
# from that URL using urllib and then parse and extract
# the comment counts from the XML data, compute the sum
# of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter location: ")
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
counter = 0
for item in lst:
	number = item.find('count').text
	counter += int(number)
print("sum:",counter)