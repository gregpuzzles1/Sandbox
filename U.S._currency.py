from __future__ import division

def find_change(amount):
    # find the amount of change in these denominations
    fifties = int(amount/50)
    twenties = int((amount-(50*fifties))/20)
    tens = int((amount-(50*fifties)-(20*twenties))/10)
    fives = int((amount-(50*fifties)-(20*twenties) \
            -(10*tens))/5)
    ones = int((amount-(50*fifties)-(20*twenties) \
           -(10*tens)-(5*fives))/1)
    change = amount - int(amount)
    qtrs = int(change/.25)
    dimes = int((change-(.25*qtrs))/.10)
    nickels = int((change-(.25*qtrs)-(.10*dimes))/.05)
    pennies = int(round((change-(.25*qtrs)-(.10*dimes) \
              -(.05*nickels))/.01))
    return fifties, twenties, tens, fives, ones, qtrs, dimes, \
           nickels, pennies

def main():
    # The main program
    try:
        x = input('Enter an amount not exceeding 99.99 (i.e. $27.34) : $')
    except (Exception):
        print "Please enter the dollar amount again."
        
    try:
        y = find_change(x)
        print "fifties = ", y[0]
        print "twenties = ", y[1]
        print "tens = ", y[2]
        print "fives = ", y[3]
        print "ones = ", y[4]
        print "quarters = ", y[5]
        print "dimes = ", y[6]
        print "nickels = ", y[7]
        print "pennies = ", y[8]
    except (Exception):
        print "There has been an error."





if __name__ == '__main__':
    main()
