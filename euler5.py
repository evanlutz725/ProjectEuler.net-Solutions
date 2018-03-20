#Project Euler: Problem 5; status-complete
#Find the smallest number such that it is divisible by all integers between 1 and 20.

x=209
while True:
	if x%11==0 and x%12==0 and x%13==0 and x%14==0 and x%15==0 and x%16==0 and x%17==0 and x%18==0 and x%19==0 and x%20==0:
		print ("Here's the number! ", x)
		break
	else:
		x=x+209
		