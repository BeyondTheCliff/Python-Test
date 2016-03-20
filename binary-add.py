import sys

Fnumber="001010" #10
Snumber="000100" #4
Onumber=[0,0,0,0,0,0]
print Fnumber + " : " + Snumber
Fnumber = map(int,str(Fnumber))
Snumber = map(int,str(Snumber))
carry=0
maxlenght=0
print Fnumber
print Snumber
if len(Fnumber)>len(Snumber):
 	maxlenght=len(Fnumber)
else:
	maxlenght=len(Snumber)
maxlenght=maxlenght-1
print maxlenght
for x in xrange(maxlenght,0,-1):
	sys.stdout.write(str(x))
	if Fnumber[x]+Snumber[x]==2:
		print " : Carry"
		Onumber[x]=0
		if carry==1:
			Onumber[x]=1
		carry=1
	if Fnumber[x]+Snumber[x]==1:
		print " : Down"
		Onumber[x]=1
		if carry==1:
			Onumber[x]=0
			carry=1
		else:
			carry=0
	if Fnumber[x]+Snumber[x]==0:
		print " : Nil"
		Onumber[x]=0
		if carry==1:
			Onumber[x]=1
		carry=0
	
print Onumber