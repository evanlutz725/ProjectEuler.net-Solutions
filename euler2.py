#Project Euler: Problem 2; status-complete
#Find the sum of the even Fibonacci sequence outputs below 4 million.

#Fibonacci Sequence starts with 1 and 2
x=1
y=2
#3 is the sum of 1 and 2
z=3
#sum starts at 2 because it is even but needs to be included
sum=2
while z<4000000:
	z=x+y
	a=z/2
	b=int(z/2)
	if a==b:
		sum=sum+z
	x=y
	y=z
	#print(z)
	
print (sum)