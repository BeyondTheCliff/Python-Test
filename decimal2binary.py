def D2B(number):
	import math

	binary = []
	iterations = 0
	
	iterations = int(math.ceil(math.log(number+1,2)))
	
	for x in xrange(iterations-1,-1,-1):
		if number-(2**x)>-1:
			binary.append("1")
			number=number-(2**x)
		else:
			binary.append("0")

	return binary