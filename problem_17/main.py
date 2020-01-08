#!/usr/bin/python
# Project Euler Problem 17. Solution: 21124

singles = {1:'one',2:'two',3:'three',4:'four',5:'five',\
        6:'six',7:'seven',8:'eight',9:'nine'}
teens = {11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',\
        15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',\
        19:'nineteen'}
tens = {10:'ten',20:'twenty',30:'thirty',40:'forty',50:'fifty',\
        60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
hundreds = {100:'onehundred',200:'twohundred',300:'threehundred',\
        400:'fourhundred',500:'fivehundred',600:'sixhundred',\
        700:'sevenhundred',800:'eighthundred',900:'ninehundred'}

def conv_num_to_words(number):
    num_str = str(number)
    if len(num_str) == 1:
        return len(singles[number])
    elif len(num_str) == 2:
        if number == 10:
            return len(tens[10])
        else:
            if int(num_str[0]) == 1:
                return len(teens[number])
        if int(num_str[1]) == 0:
            return len(tens[number])
        else:
            return len(tens[(int(num_str[0])*10)]) + len(singles[int(num_str[1])])
    elif len(num_str) == 3:
        start_str = len(hundreds[(int(num_str[0])*100)])
        if num_str[1:] == '00':
            return start_str
        if int(num_str[1]) == 0:
            end_str = conv_num_to_words(int(num_str[2]))
            return start_str+end_str+3
        else:
            end_str = conv_num_to_words(int(num_str[1:]))
            return start_str+end_str+3
    else:
        return 11

total = 0
for i in range(1,1001):
    try:
        total += conv_num_to_words(i)
    except:
        import traceback
        print traceback.format_exc()
        print i
        exit()
print total
