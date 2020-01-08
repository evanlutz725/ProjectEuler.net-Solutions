#!/usr/bin/python
# Project Euler problem 11. Solution: 76576500
import copy
import math
count = 1
triangle_num = 0
while True:
    triangle_num += count
    divisors_count = 0
    for test_num in range(1,(int(math.sqrt(triangle_num))+1)):
        if triangle_num % test_num == 0:
            divisors_count += 1

    if divisors_count*2 > 500:
        print 'Winner! %s' %triangle_num
        exit()
    else:
        print triangle_num, divisors_count
        count += 1
