number = {
    1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
    8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
    14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
    18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',
    50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
    100:'hundred',1000:'thousand'}

x = input('Please enter an number between 1 and 1000: ')
x1 = str(x)
if len(x1) == 1:
    # If user enters a number between 1-9
    print "Integer in English is: ",  number[x]
elif len(x1) == 2:
    # If user enters a number between 10-99
    x2 = x1[0:1]
    x3 = x1[1:2]
    if x < 20:
        # Consider numbers less than 20
        print "Integer in English is: ", number[x]
    elif x2 != '0' and x3 == '0':
        # Consider multiples of 10: 20, 30 ...
        print "Integer in English is: ", number[x]
    else:
        # Consider all other numbers less than 100
        x4 = str(x2 + '0')
        print "Integer in English is:", number[int(x4)] + \
              '-' + number[int(x3)]
elif len(x1) == 3:
    # If user enters a number between 100-999
    x2 = x1[0:1]
    x3 = x1[1:2]
    x4 = x1[2:3]
    x5 = (x3 + x4)
    x6 = x3 + '0'
    if x3 == '0' and x4 == '0':
        # Consider the 100, 200, 300 numbers ...
        print "Integer in English is:", number[int(x2)] \
              + '-' + number[100]
    elif x3 == '0' and x4 != '0':
        # Consider 101-109, 201-209, ...
        print "Integer in English is:", number[int(x2)]+ \
              '-' + number[100] + ' and ' + number[int(x4)]
    elif x3 != '0' and x4 == '0':
        # Consider 110,120,130, 210,220,230 ...
        print "Integer in English is:", number[int(x2)] \
              + '-' + number[100] + ' and ' + number[int(x5)]
    elif x3 == '1' and x4 != '0':
        # Consider the teens 111-119, 211-219 ...
        print "Integer in English is:", number[int(x2)] \
              + '-' + number[100] + ' and ' + number[int(x5)]
    else:
        # Consider all other 3 digit numbers
        print "Integer in English is:", number[int(x2)] \
              + '-' + number[100] + ' and ' + number[int(x6)] \
              + '-' + number[int(x4)]
elif len(x1) == 4 and x == 1000:
    # If user enters 1000
    print "Integer in English is:", number[1] + '-' + number[1000]
else:
    # If user enters something other than a number from 1-1000
    print "Please try again"

