#!/usr/bin/python
# Project Euler Problem 11. Solution: 70600674 and a product of ['89', '94', '97', '87']
f = open('numbers.txt')
numbers_array = []
for row in f:
    row = row.rstrip()
    row = row.split()
    numbers_array.append(row)
max_prod = [0,[]]
for count,row in enumerate(numbers_array):
    if count < 17:
        # test vertical products
        for vert_position in range(20):
            num_one = numbers_array[count][vert_position]
            num_two = numbers_array[count+1][vert_position]
            num_three = numbers_array[count+2][vert_position]
            num_four = numbers_array[count+3][vert_position]
            print num_one, num_two, num_three, num_four
            test_product = int(num_one) * int(num_two) * int(num_three) * int(num_four)
            print test_product
            if test_product > max_prod[0]:
                max_prod = [test_product,[num_one,num_two,num_three,num_four]]
        # test diagonials
        for vert_position in range(17):
            num_one = numbers_array[count][vert_position]
            num_two = numbers_array[count+1][vert_position+1]
            num_three = numbers_array[count+2][vert_position+2]
            num_four = numbers_array[count+3][vert_position+3]
            print num_one, num_two, num_three, num_four
            test_product = int(num_one) * int(num_two) * int(num_three) * int(num_four)
            print test_product
            if test_product > max_prod[0]:
                max_prod = [test_product,[num_one,num_two,num_three,num_four]]
        # test antidiagonials
        for vert_position in range(3,20):
            num_one = numbers_array[count][vert_position]
            num_two = numbers_array[count+1][vert_position-1]
            num_three = numbers_array[count+2][vert_position-2]
            num_four = numbers_array[count+3][vert_position-3]
            print num_one, num_two, num_three, num_four
            test_product = int(num_one) * int(num_two) * int(num_three) * int(num_four)
            print test_product
            if test_product > max_prod[0]:
                max_prod = [test_product,[num_one,num_two,num_three,num_four]]

    for horiz_position in range(17):
        num_one = numbers_array[count][horiz_position]
        num_two = numbers_array[count][horiz_position+1]
        num_three = numbers_array[count][horiz_position+2]
        num_four = numbers_array[count][horiz_position+3]
        test_product = int(num_one) * int(num_two) * int(num_three) * int(num_four)
        print test_product
        if test_product > max_prod[0]:
            max_prod = [test_product,[num_one,num_two,num_three,num_four]]
print max_prod

