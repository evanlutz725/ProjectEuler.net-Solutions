#Project Euler: Problem 3; status-complete
#Find the largest prime divisor of 600851475143.

#based on a function shared on StackOverflow
def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True
        
       
prime_divisors=[0]
x=2
a=600851475143
b=100
while x<a:
	if is_prime(x) is True and a%x==0:
		prime_divisors.append(x)
		print (prime_divisors)
        
	x+=1