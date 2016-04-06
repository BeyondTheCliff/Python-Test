import random
import matplotlib.pyplot as plt
import numpy

matrix = [[0 for x in range(10)] for x in range(10)] 
xvar=0
yvar=0
nmax=1000

for i in xrange(1,nmax):
	xvar=random.randrange(0,9)
	yvar=random.randrange(0,9)
	matrix[xvar][yvar]=matrix[xvar][yvar]+1

for x in xrange(0,9):
	print matrix[x]

plt.plot(matrix, interpolation='nearest', cmap=plt.cm.ocean,
    extent=(0.5,numpy.shape(matrix)[0]+0.5,0.5,numpy.shape(matrix)[1]+0.5))
plt.show()