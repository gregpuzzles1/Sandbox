"""def sum(lower, upper, margin):
    for x in range(margin): print " ",
    print lower, upper
    if lower > upper:
        for x in range(margin): print " ",
        print 0
        return 0
    else:
        result = lower + sum(lower + 1, upper, margin + 2)
        for x in range(margin): print " ",
        print result
        return result

"""

def sum(lower, upper, margin):
    blanks = " " * margin
    print blanks, lower, upper
    if lower > upper:
        print blanks, 0
        return 0
    else:
        result = lower + sum(lower + 1, upper, margin + 4)
        print blanks, result
        return result
    
