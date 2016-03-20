import matplotlib.pyplot as plt

print("Starting")

population=4
generations=250
children=0
pop_array=[]
gen_array=[]
chd_array=[]
pop_array.append(population)
gen_array.append(0)
chd_array.append(0)
print "Generation: 0 :","Population:",population,": Children:",children

for x in xrange(1,generations+1):
	population=population+children
	children=(population-population%2)/2
	print "Generation:",x,":","Population:",population,": Children:",children
	pop_array.append(population)
	gen_array.append(x)
	chd_array.append(children)
	if population>99:
		population=population*0.2
	population = int(population)
	children = int(children)


plt.plot(gen_array,pop_array,'r--',gen_array,chd_array,'b--')
plt.ylabel('Population')
plt.xlabel('Generations')
plt.show()
