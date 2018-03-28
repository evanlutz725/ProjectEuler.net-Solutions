#Project Euler: Problem 9; status-complete
#Find the Pythagorean triplet such that a+b+c=1000.

p_triplets=[]
a=2
def p_trip_funct(num):
	"""Returns True if the number is a Pythagorean triple
	else False."""
	for x in range(1, num):
		if (x**2+num**2)**.5==int((x**2+num**2)**.5):
			y=int((x**2+num**2)**.5)
			p_triplets.append([x,num,y])
		if x==num-1:
			return True
			
while a<500:
	if p_trip_funct(a) is True:
		a+=1
		

				
z=0
while True:
	if p_triplets[z][0] + p_triplets[z][1] + p_triplets[z][2] == 1000:
		print (p_triplets[z])
		print ("The product of these three numbers is ", p_triplets[z][0] * p_triplets[z][1] * p_triplets[z][2], ".")
		break
	z+=1