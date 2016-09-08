# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 18:00:41 2016

@author: nightduck
"""

# adjList = [(num,[num,num,...]), (num, [num, num,...]),...]

#User notes
print "About this program:"
print "This script takes a list of number pairs corresponding to edges and outputs"
print "a gml file. The list doesn't have to be sorted, but it is recommended that"
print "unique node numbers are fairly consecutive. IE (1,2,4,5,6,9,10), and not"
print "(1,56,356,824). If spare time is given, try rewriting the script to use"
print "dictionaries for adjList. Also, the script doesn't acknowledge hypens in"
print "filenames."

##Input file here
filename = raw_input("Input file: ")
f = open(filename, 'r')


adjList = []

for line in f:
	nums = [int(s) for s in line.split()]
	
	#Try to store each number in a matching index, so expand adjList so that index exists
	while(nums[0] > len(adjList)-1):
		adjList.append(0)
	while(nums[1] > len(adjList)-1):
		adjList.append(0)

	#
	if (adjList[nums[0]] == 0):
		adjList[nums[0]] = (nums[0], [nums[1]])
	else:
		adjList[nums[0]][1].append(nums[1])
		
	if (adjList[nums[1]] == 0):
		adjList[nums[1]] = (nums[1], [])
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
