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
objects=[a,b,c,time]
limit=61
a[0].speed=10
for x in xrange(1,limit):
   time.append(x)
   a.append(Update(10,1,a[x-1].speed))
   print str(a[x-1].speed)

plt.plot(time,a,'r--')
plt.show()