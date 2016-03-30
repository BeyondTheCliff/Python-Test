#import matplotlib.pyplot as plt

population = [20,20]
generations = 5



for x in xrange(1,generations):
	for i in xrange(0,len(population)):
		population[i]=population[i]+1
