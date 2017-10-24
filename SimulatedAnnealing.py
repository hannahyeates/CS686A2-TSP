
# THE FOLLOWING WEBSITE WAS USED FOR HELP WTIH 
# UNDERSTANDING THE SIMULATED ANNEALING ALGORITHM:
#http://katrinaeg.com/simulated-annealing.html

'''
	This file contains everything related to the 
	Simulated Annealing algorithm. 
'''

import TSPutils as tsp
import AnnealingSchedules as sc
import random
import math
import copy


# this function performs a two swap by swapping 
# two random cities along the tour
def TwoSwap(tour):
	idx1 = random.randrange(1,len(tour.path)-2)
	idx2 = random.randrange(1,len(tour.path)-2)
	newPath = copy.deepcopy(tour.path)
	newPath[idx2] = tour.path[idx1]
	newPath[idx1] = tour.path[idx2]
	return newPath

# Helper function to return if t2 is shorter than t1
def isShorter(t1, t2):
	if t1.length < t2.length :
		return False
	return True

# Helper function to calculate the acceptance probability
# given a T value
def calcAcceptanceProbability(t1, t2, T):
	return math.exp(-(t2.length-t1.length)/T)


'''
	Given a set of initial parameters, this method will run the 
	Simulated annealing algorithm and return the shortest cost 
	that was found by the program. 
	NOTE: the 'trackCost' parameter indicates whether or not we are 
	interessted in listing the tour costs as they decrease
'''
def simulatedAnnealing(cities, schedule, T_init, alpha, trackCost):
	path = tsp.buildInitialTour(cities)
	tour = tsp.tour(path)
	tour.calcLength(cities)
	costs = []
	T = T_init
	
	# Tracks the number of assignments that we make while running the program	
	k = 0
	while T > 0:	
		testTour = tsp.tour(TwoSwap(tour))
		testTour.calcLength(cities)
		# move to the shorter path with probability 1
		if isShorter(tour, testTour):
			tour = testTour
			costs.append([tour.length])
			k += 1
		else: 
			# stopping condition for if the different between
			# tours is too small for the program to identify	
			if tour.length - testTour.length == 0 :
				break	
			
			p =  calcAcceptanceProbability(tour, testTour, T)
			
			# move with probability p if testTour is worse than tour
			if random.random() < p:
				tour = testTour
				costs.append([tour.length])
				k+=1
		T = sc.calcT(T, k, schedule, alpha)
	return [tour, k, costs]