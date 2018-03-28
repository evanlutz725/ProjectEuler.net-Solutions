#Project Euler: Problem 20; status-complete
#Find the sum of digits of 100!.

import math
a=math.factorial(100)
b=str(a)
c=[]
for x in b:
	c.append(int(x))
print(sum(c))
