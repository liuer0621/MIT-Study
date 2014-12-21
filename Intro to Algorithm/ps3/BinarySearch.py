#!/usr/bin/env python

data = []

for i in range(100) :
	data.append(i)


#binary search function
def binary_search(searchList,key):
	min = 0
	max = len(searchList) - 1

	while True:

		middle = int((min+max) // 2)
		print "middle number is %d",middle
		
		if key < searchList[middle] :
			max = middle - 1 
		elif key > searchList[middle] :
			min = middle + 1
		elif key == searchList[middle] :
			print middle,searchList[middle]
			return middle 

		
number = input('Enter the number you wanna search: ')
binary_search(data,number)


