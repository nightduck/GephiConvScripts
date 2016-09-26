# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 18:00:41 2016

@author: nightduck
"""

# adjList = [num : [num,num,...]), num : [num, num,...]),...]
# For node pairs that are of a form other than numbers, edit line 20

##Input file here
filename = raw_input("Input file: ")
f = open(filename, 'r')

#Adjacency list
adjList = {}

for line in f:
	#Extract each number in line to be in a list. This list will only have 2 numbers
	nums = [int(s) for s in line.split()] #If you want to do something other than number pairs, remove the int() and leave just s

	#Using the first number as a key corresponding to a list of adjacent nodes, add the second number to that list
	if nums[0] not in adjList:
		adjList[nums[0]] = [nums[1]]
	else:
		adjList[nums[0]].append(nums[1])
		
	#If the second num not in the adjList, make a key/value pair for it with an empty list
	if nums[1] not in adjList:
		adjList[nums[1]] = []
f.close()

#Output file here
filename = raw_input("Output file: ")
f = open(filename, 'w')


f.write("graph [\n")

for x in adjList:
	if (x != 0):
		f.write("\tnode [\n\t\tid " + str(x[0]) + "\n\t]\n")
	
for x in adjList:
	if (x != 0):	
		for y in x[1]:
			f.write("\tedge [\n\t\tsource " + str(x[0]) + "\n\t\ttarget " + str(y) + "\n\t\tvalue 1\n\t]\n")

f.write("]")
f.close()
