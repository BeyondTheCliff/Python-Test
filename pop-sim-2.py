#import matplotlib.pyplot as plt
import random

population = [20,20]
generations = 5



for x in range(1,generations):
	for i in range(0,len(population)):
		population[i]=population[i]+1
		print population[i]
	#for j in xrange(1,len(population)/2):
			#population.append()
