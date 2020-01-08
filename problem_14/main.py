#!/usr/bin/python
# Project Euler Problem Number 14. Solution: 837799 with 525 steps
def is_even(test_num):
    if test_num % 2 == 0:
        return True
    else:
        return False

def calc_lattice(start_num):
    #print 'Test Value: %s' %(rolling_num)
    count = 0
    rolling_num = start_num
    while True:
        #print rolling_num
        if rolling_num == 1:
            count += 1
            return count
        if rolling_num < start_num:
            #print 'Dict Entry Found: %s' %rolling_num
            #print 'Dict Value: %s' %record_dict[rolling_num]
            count += record_dict[rolling_num]
            return count
        if is_even(rolling_num):
            rolling_num = rolling_num/2
            count += 1
        else:
            rolling_num = 3*rolling_num+1
            count += 1

record_dict = {}
test_value = 1

while test_value <= 1000000:
    count = calc_lattice(test_value)
    print test_value,count
    record_dict[test_value] = count
    test_value += 1

highest_key = 0
highest_value = 0
for key in record_dict.keys():
    if record_dict[key] > highest_value:
        highest_key = key
        highest_value = record_dict[key]

print('\n\nHighest Value:\n')
print highest_key,highest_value

