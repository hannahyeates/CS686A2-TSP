'''
	This file contains all of the TSP specific code
	used in the Simulated Annealing Algorithm. 

'''

import scipy.spatial as sp


# Class that contains a complete tour
class tour(object):
	def __init__(self, path):
		self.path = path
		self.length = 0

	#Calculates the distance of the entire tour
	def calcLength(self, cities):
		tourLength = 0
		for i in range(0, len(self.path)-1) : 
			tourLength += distance(cities[self.path[i]]['x'], cities[self.path[i]]['y'], cities[self.path[i+1]]['x'], cities[self.path[i+1]]['y'])
			print self.path[i] + ',' + self.path[i+1]
		self.length = tourLength


# Calculates the euclidean distance between two cities
def distance(x_start, y_start, x_end, y_end):
	return sp.distance.euclidean([x_start, y_start], [x_end, y_end])

#loads the list of cities with (x,y) coordinates into a dictionary
def loadInstance(path):
	allNodes = {}
	numNodes = 0
	file = open(path, 'r')
	for line in file:
		tmp = line.split()
		if(len(tmp) == 1):
			numNodes = tmp[0]
		else:
			allNodes[tmp[0]] = {'x': int(tmp[1]), 'y': int(tmp[2])}
	if(len(allNodes) == int(numNodes)):
		return allNodes
	else: 
		print "input error, could not complete execution"
		sys.exit()


# Builds the initial tour from the set of cities		
def buildInitialTour(cities):
	tour = ['A']
	for city in cities:
		if city <> 'A':
			tour.append(city)
	tour.append('A')
	return tour

