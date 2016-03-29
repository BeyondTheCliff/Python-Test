import random

top=20**5000
number=1

while number<top:
	number = random.randint(1,10)*random.randint(1,10)*number+random.randint(1,10)
	print number
	print "----------------------------------------"

print number
print "------------2--------2------------------"
print number/2
print "-------------3--------3-----------------"
print number/3