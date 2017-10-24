'''
	This is the file that I used to run all of the experiments to 
	determine which annealing schedule performed the best. 
	This runs each annealing schedule with a starting T value of 
	5000, and by decrementing alpha by 0.1 every 100 runs.

'''
import csv
import TSPutils as tsp
import SimulatedAnnealing as sa
import numpy
import time

annealingSchedules = [
	'linear',
	'exponential' ,
	'logarithmic' ,
	'quadraticMultiplicative',
	'linearMultiplicative' 
]

#initialize all variables
path = 'randTSP/problem36.txt'
cities = tsp.loadInstance(path)
T_init = 5000
data = []
tourLength = []
avgTourLength = []

#iterate over all annealing schedules to get data on all alpha values
for schedule in annealingSchedules:
	alpha = .99
	while alpha > 0:
		startTime = time.time()
		# run the simulated annealing algorithm with the specified values 100 times
		for i in range(100): 
			results = sa.simulatedAnnealing(cities, schedule, T_init, alpha, False)
			tourLength.append(results[0].length)
		runtime = time.time() - startTime
		avgTourLength.append([runtime, schedule,alpha,numpy.mean(tourLength)])
		alpha -= 0.1
		print alpha
	
	## Write to the file for the specified annealing schedule
	myfile = open(schedule + '_'+ str(alpha) + '_TSP.csv', 'w') 
	with myfile:
		writer = csv.writer(myfile)
		writer.writerows(avgTourLength)	
	data = []
	tourLength = []
	avgTourLength = []