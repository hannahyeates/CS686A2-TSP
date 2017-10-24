'''
	This code was used to graph the tour of the shortest path found, 
	it can be used for any path outputted by the SASimulation.py
'''

import csv
import numpy
import matplotlib.pyplot as pyplot
import TSPutils as tsp

f = open('path.csv')
cities = tsp.loadInstance('randTSP/problem36.txt')
path = None
for row in csv.reader(f):
	path = row
newPath = []

#strip off extra quotation marks from the cities
for city in path:
	newPath.append(city.strip().strip('\''))

tour = tsp.tour(newPath)
tour.calcLength(cities)
print tour.length

# Build plot using the pyplot library
x_values = []
y_values = []
for city in newPath:
	x_values.append(cities[city]['x'])
	y_values.append(cities[city]['y'])

x = numpy.array(x_values)
y = numpy.array(y_values)
pyplot.plot(x,y,  marker='o')
pyplot.ylim(-20,120)
pyplot.xlim(-20,120)

for i, label in enumerate(newPath): 
   pyplot.text (x[i], y[i], label ) 


pyplot.show()

