
a="0"
b="1"
x,y=[0,0],[0,0]
ans=[x,y]

if a=="1":
	x[0]=1
	y[0]=1
else:
	x[1]=1
	y[1]=1

if b=="1":
	x[0]=1
	x[1]=1
else:
	y[0]=1
	y[1]=1

print x
print y