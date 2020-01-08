#!/usr/bin/python
tree = {}
row_num = 0
for row in open('tree.txt'):
    row = [int(i) for i in row.split()]
    tree[row_num]=row
    row_num += 1
current_total = tree[0][0]
current_index = 0
try:
    for row in range(1,15):
       left_sum =  current_total
       right_sum = current_total
       left_index = current_index
       for i in range(row,15):
           left_sum += tree[i][left_index]
       print 'left_sum: %s ' %left_sum
       right_index = current_index + 1
       for i in range(row,15):
           right_sum += tree[i][right_index]
           right_index += 1
       print 'right_sum: %s ' %right_sum
       if left_sum > right_sum:
           print 'left wins: %s ' %tree[row][current_index]
           current_total += tree[row][current_index]
       else:
           print 'right wins: %s ' %tree[row][current_index+1]
           current_total += tree[row][current_index +1]
           current_index += 1
    print 'winner: %s ' %current_total
except:
    import traceback
    print traceback.format_exc()
    import pprint
    pprint.pprint(locals())
