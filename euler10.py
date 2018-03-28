#Project Euler: Problem 10; status-complete
#Find the sum of primes lower than 2000000.
#On my PC, total runtime apx 70 seconds.
import timeit
start=timeit.default_timer()
def is_prime(num):
	"""Returns True if the number is prime
	else False."""
	for x in range(2, int(num**.5)+1):
		if num % x == 0:
			return False
	else:
		return True
		
		
		
primes=[]
x=2
sum=0
while x<2000000:
	if is_prime(x) is True:
		sum+=x
	x+=1

	


print (sum)
stop=timeit.default_timer()
print(stop-start)