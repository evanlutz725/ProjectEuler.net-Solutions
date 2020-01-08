#!/usr/bin/python
#Project Euler Number 13: solution 5537376230
f = open('numbers.txt')
numbers_array = [number.rstrip() for number in f]
for _ in range(40):
    trailing_sum = 0
    for number in numbers_array:
        if number:
            print number
            trailing_const = int(number[-1:])
            trailing_sum += trailing_const
    numbers_array.append(str(trailing_sum))
    new_array = [number[:-1]for number in numbers_array]
    numbers_array = new_array
leading_sum = 0
print numbers_array
for number in numbers_array:
    if number:
        leading_sum += int(number)
leading_sum = str(leading_sum)
print leading_sum[0:10]
        
        
