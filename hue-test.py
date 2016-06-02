from phue import Bridge
import time

b = Bridge('10.0.1.7')

error=0
while error==0:
	print ""
	print "off:on"
	print "list"
	print "exit"
	print "Enter Command:"
	userInput=raw_input()
	if userInput=="off":
		b.set_light([1,2,3], 'on', False)
	if userInput=="on":
		b.set_light([1,2,3], 'on', True)
	if userInput=="list":
		lights = b.lights
		for l in lights:
			print(l.name)
	if userInput=="exit":
		exit()



#print b.get_api()