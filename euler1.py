#Project Euler: Problem 1; status-complete
#Find the sum of all numbers below 1000 that are divisible by either 3 or 5 but not both.

x=1
sum=0
while x<1000:
	a=x/3
	b=int(x/3)
	if a==b:
		sum=sum+x
		#print (x)
	x=x+1

	
sum1=0
y=1
while y<1000:
	c=y/5
	d=int(y/5)
	e=y/3
	f=int(y/3)
	if c==d and not e==f:	
		sum1=sum1+y
		#print (y)
	y=y+1
	

print (sum1+sum)

