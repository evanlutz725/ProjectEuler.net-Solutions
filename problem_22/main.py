#!/usr/bin/python3
# Project Euler Problem 22. Solution: 871198282

from names import NAMES

NAMES = sorted(NAMES)

letter_conv_dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def conv_letter_to_num(letter):
    return letter_conv_dict[letter]

total = 0

for position in range(1,len(NAMES)+1):
    name = NAMES[position-1]
    for letter in name:
        total += position*conv_letter_to_num(letter)

print(total)

