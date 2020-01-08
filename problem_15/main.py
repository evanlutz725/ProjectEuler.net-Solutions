#!/usr/bin/python
# Project Euler Problem 15. Solution: 137846528820
def C(n,r):
    total = factorial(n)/(factorial(r)*factorial(n-r))
    return total

def factorial(integer):
    total = 1
    for i in range(1,integer+1):
        total *= i
    return total

print C(40,20)
