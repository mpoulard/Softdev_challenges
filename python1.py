#!/usr/bin/python

import re
import copy
import sys

# Open the file
f = open("test1.txt", "rw+")


#Initialization
data = []
index = []
dataOrder = '\n'


#Creating the list of index with the good order
for line in sys.stdin:
	number = re.search("(\d)+",line).group()
	data.append(line)
	index.append(number)



indexOrder = copy.copy(index)
indexOrder = list(set(indexOrder))
indexOrder.sort()
indexOrder.reverse()




#Printing the good lines
for i in range(int(sys.argv[1])):
	for j in range(len(index)):
		if indexOrder[i] == index[j]:
			#print data[j]
			dataOrder = dataOrder + str(data[j]) + ''

print dataOrder
			
	

