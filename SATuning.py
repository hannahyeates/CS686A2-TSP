'''
	This file was used to tune the parameters for simulated annealing
	to find which ones would consistently produce the smallest values. 
	The Tuning started the T_init at 10000 and slowly reduced it 
	to 1799, which was the largest value that was found using the 
	logarithmic cooling schedule. This program also reduces alpha from 
	0.99 to 0.29 to determine which combination of parameters would produce 
	shortest path. 

	This file will output the shortest path found in the 1000 runs.
'''


import csv
import TSPutils as tsp
import SimulatedAnnealing as sa
import numpy
import time

path = 'randTSP/problem36.txt'
cities = tsp.loadInstance(path)

#Inititalize data collection and tuning parameters
data = []
shortestTour = []
# stores how the costs of the move decrease as time goes on 
decreasingCosts = []
schedule = 'logarithmic'
T_init = 10000


# iterate over alpha and T_init to find best parameters. 
while T_init > 1799:
	alpha = 0.99
	while alpha > 0.28:
		for i in range(10):
			startTime = time.time()
			# Collect results from the simulated annealing algorithm
			results = sa.simulatedAnnealing(cities, schedule, T_init, alpha, True)
			runtime = time.time() - startTime
			
			#store the data for the shortest path found 
			if shortestTour == []: 
				shortestTour = [runtime, alpha, T_init, results[1], results[0].length, results[0].path,1]
				decreasingCosts = results[2]
			if runtime < 300 and results[0].length <= shortestTour[4]:
				shortestTour.append([runtime, alpha, T_init, results[1], results[0].length, results[0].path,1])
				decreasingCosts.append(results[2])
		print str(alpha) + ',' + str(T_init) + ' done'
		alpha -= 0.1
	T_init -= 200


#write results to a file for further analysis
myfile = open('TSP_Tuning.csv', 'w') 
with myfile:
	writer = csv.writer(myfile)
	writer.writerows([shortestTour])	
myfile = open('MoveCosts.csv', 'w') 
with myfile:
	writer = csv.writer(myfile)
	writer.writerows(decreasingCosts)
print "done"
