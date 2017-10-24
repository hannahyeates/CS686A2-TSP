# CS686A1-TSP
# Hannah Gautreau, 20486960

The purpose of this set of programs is to Tune, and run experiments on the Simulated Annealing Program on the Travelling Salesman Problem. 
To run all instances of this program, ensure that you have the randTSP folder in the same folder as all of the code.

1) To run the Simulating Annealing Algorithm one time, run RunOnce.py
2) To run the Simulated Annealing Algorithm with ALL annealing schedules, run SAExperiments.py
3) To tune the Simulated Annealing Algorithm, run SATuning.py
4) To run the tuned Simulated Annealing Algorithm in order to find the shortest path, run SASimualtion.py. Please note that TrackCosts MUST be set to true
5) To graph the tour found, run GraphTour.py. Before running this program, copy the path from the TSP_Simulation file into a csv file called path.csv

I have also included three csv files coniaining the raw data for the shortest tour found while running the program. 

Other Tips:
	To get the shortest path possible, run the SASimulation program and update the number of iterations to the number that you would like to run