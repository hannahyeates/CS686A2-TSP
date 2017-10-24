#this file contains all of the annealing schedules that were experimented with for simulated annealing

import math

# method to route the input to the correct annealing schedule based on the input
def calcT(T, k, schedule, alpha):
	options = {
		'linear' : linear(T,k, alpha),
		'exponential' : exponential(T,k, alpha),
		'logarithmic' : logarithmic(T,k, alpha),
		'quadraticMultiplicative' : quadraticMultiplicative(T,k, alpha),
		'linearMultiplicative' : linearMultiplicative(T,k, alpha)
	} 

	return options[schedule]

def linear(T, k, alpha):
	return T - alpha*k

def exponential(T, k, alpha):
	return T*(alpha**k)

def logarithmic(T, k, alpha):
	return T/(1 + alpha * math.log1p(k))

def quadraticMultiplicative(T, k, alpha):
	return T/(1+alpha*(k**2))

def linearMultiplicative(T, k, alpha):
	return T/(1+alpha*k)
