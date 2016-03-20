import time
import math
top=10
start=time.time()
while (time.time()-start<top):
	time.sleep(0.01)
	print math.fabs(-((top+start)-time.time())**-2)

print "Done"