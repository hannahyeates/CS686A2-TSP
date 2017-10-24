'''
	This file was used to find the shortest path using my optimal parameters
	The reason that 3200 was chosen was because it produced the shortest path
	in the experiments, and was big enough that it would never be shorter than 
	a randomly generated tour. 0.29 was chosen for the alpha value because
	it was a good balance between having a small alpha without having a very 
	long run time

	This file will output the shortest path found in the 1000 runs.
'''


import csv
import TSPutils as tsp
import SimulatedAnnealing as sa
import numpy
import time

path = 'randTSP/problem36.txt'
cities = tsp.loadInstance(path)

data = []
shortestTour = []

# keeps the costs of each assignment in Simulated Annealing
decreasingCosts = []

#initialize optimal values from SA Experiments
schedule = 'logarithmic'
T_init = 3200
alpha = 0.29

# Run simulated Annealing 1000 times
for i in range(1000):
	startTime = time.time()
	results = sa.simulatedAnnealing(cities, schedule, T_init, alpha, True)
	runtime = time.time() - startTime
	# The following two if statements record the data for the new shortest path, and print it 
	# to the console 
	if shortestTour == []: 
		shortestTour = [runtime, alpha, T_init, results[1], results[0].length, results[0].path]
		decreasingCosts = results[2]
		print str(results[0].length) + ',' + str(results[0].path)
	if results[0].length < shortestTour[4]:
		shortestTour = [runtime, alpha, T_init, results[1], results[0].length, results[0].path]
		decreasingCosts = results[2]
		print str(results[0].length) + ',' + str(results[0].path)
		


# write results to file
myfile = open('TSP_Simulation.csv', 'w') 
with myfile:
	writer = csv.writer(myfile)
	writer.writerows([shortestTour])	
myfile = open('MoveCosts_Simulation.csv', 'w') 
with myfile:
	writer = csv.writer(myfile)
	writer.writerows(decreasingCosts)
