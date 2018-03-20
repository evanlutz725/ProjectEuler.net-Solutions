#Project Euler: Problem 7; status-complete
#Find the 10001th prime number.

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
        
        
primes=[]
y=1
x=2
while y<10002:
    if is_prime(x) is True:
        primes.append(x)
        y+=1
    x+=1

    

print ("The 10001th prime number is ", primes[-1])