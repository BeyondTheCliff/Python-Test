from graphics import *
import time
import random
import thread

win = GraphWin()
pt=[]
randsx=[]
randsy=[]
maxn=10000
for x in xrange(0,maxn):
	randsx.append(random.randrange(0,200))
	randsy.append(random.randrange(0,200))
print "Randoms Done"
def dispOut(start,end):
	for x in xrange(start,end):
		pt.insert(Point(randsx[x],randsy[x]),x)
		pt[x].draw(win)

try:
   thread.start_new_thread( dispOut, (0,5000) )
   thread.start_new_thread( dispOut, (5001,10000) )
except:
   print "Error: unable to start thread"

print "Done"
win.close()
#print "Hit Enter:"
#userInput=raw_input()

