import math
import matplotlib.pyplot as plt

class Update:
   def __init__(self, mass, force, speed):
      self.mass = mass
      self.force = force
      self.acceleration = mass*force
      self.speed = speed + self.acceleration

class Trig(object):
   def __init__(self, i, resolution, offset):
      self.i=i
      self.resolution=resolution
      self.offset=offset
      self.outputX=math.cos(i/resolution-offset)  
      self.outputY=math.sin(i/resolution-offset)

def dump(obj):
         for attr in dir(obj):
            print "obj.%s = %s" % (attr,getattr(obj,attr))

a=[]
b=[]
c=[]
time=[]
XVAR=[]
YVAR=[]
objects=[a,b,c,time]
limit=61
for x in xrange(1,limit):
   time.append(x)
   a.append(Update(1,10*x,0-x))
   b.append(Update(2,10*x,0-x))
   c.append(Trig(x,limit/(math.pi*2),0))
   XVAR=c[x-1].outputX
   YVAR=c[x-1].outputY
   print str(c[x-1].outputX) + " : " + str(c[x-1].outputY)
   print

plt.plot(XVAR,YVAR,'r--')
plt.show()