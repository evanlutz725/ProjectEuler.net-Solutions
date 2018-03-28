#Project Euler: Problem 21; status-complete
#Find the sum of all amicable numbers below 10000.
#Two numbers are an amicable pair if the sum of a's divisors = b
#and the sum of b's divisors = a and a!=b
#On my PC, total runtime apx 22 seconds.

import timeit
start=timeit.default_timer()

num_div_sum_dict={}
test_no=1
amicable_sum=0
#this loop is designed to make a dictionary entries like 220:285,
#where 220 is the tested number and 285 is the sum of all its divisors, excluding 220.
while test_no<10000:
	test_no_div_sum=0
	test_div=1
	while True:
		if test_no%test_div==0:
			test_no_div_sum+=test_div
		if test_div>test_no/2:
			num_div_sum_dict[test_no]=test_no_div_sum
			break
		test_div+=1
	test_no+=1

count=0
#makes list of keys with maintained order to utilize "count" reference in next loop.	
dict_keys=sorted(num_div_sum_dict.keys())
#This loop assigns y to the key position being tested,
#assigns x to the dict entry of y, then tests iff x is in dict.
while count<len(num_div_sum_dict):
	y=dict_keys[count]
	x=num_div_sum_dict[y]
	if x in num_div_sum_dict:
		if num_div_sum_dict[x]==y and x!=y:
			amicable_sum+=x
	count+=1
	
	
print(amicable_sum)

stop=timeit.default_timer()
print(stop-start, "= Total Runtime")