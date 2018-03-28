#Project Euler: Problem 16; status-complete
#Find the sum of digits of 2**1000.

a=2**1000
b=str(a)
c=[]
for x in b:
	c.append(int(x))
print(sum(c))
