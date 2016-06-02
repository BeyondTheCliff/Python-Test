class D2B(object):
	"""docstring for D2B"""
	def __init__(self, number):
		math = __import__('math')
		self.number = number
		self.binary = ""
		self.iterations = int(math.ceil(math.log(number+1,2)))

	def convert(self):
		for x in xrange(self.iterations-1,-1,-1):
			if self.number-(2**x)>-1:
				self.binary+="1"
				self.number=self.number-(2**x)
			else:
				self.binary+="0"

class B2D(object):
	"""docstring for B2D"""
	def __init__(self, binary):
		math = __import__('math')
		self.binary = str(binary)
		self.number = 0
		self.iterations = len(self.binary)

	def convert(self):
		for x in xrange(0,self.iterations):
			if self.binary[x]=='1':
				self.number=self.number+(2**self.iterations)
				self.iterations=self.iterations-1
			if self.binary[x]=="0":
				self.number=self.number
				self.iterations=self.iterations-1
		

#objects=[]
#for x in xrange(0,33):
#	objects.append(D2B(x))
#	objects[x].convert()
#	print objects[x].binary + ":" + str(objects[x].iterations)
object1=B2D(1)
object1.convert()
print object1.number
object2=D2B(object1.number)
object2.convert()
print object2.binary
object3=B2D(object2.binary)
object3.convert()
print object3.number