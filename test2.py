import matplotlib.pyplot as plt
import numpy as np

data=[]
time=[]
for x in xrange(1,100):
	data.append(np.sin(x/10))
	print np.sin(x)
	time.append(x)

plt.plot(time,data,'b--')
plt.show()