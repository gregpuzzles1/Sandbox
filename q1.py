import random

g = input('How many points to win?: ')
n = input('What is the maximum number of turns?: ')

def roll_die():
    # Roll the die
    return random.randint(1,6)

def play_single_turn(total):
    # Play a single turn
    play = 'y'
    turn_total = 0
    while play != 'h':
        y = roll_die()
        if y == 1:
            # Turn over - got a 1!
            turn_total = 0
            print "Total points:\t", total
            print "Roll:\t", y
            print "Your turn is over!"
            print "Turn total: \t", turn_total
            print raw_input("Press <Enter> to continue... ")
            play = 'h'
        else:
            # Play turn
            turn_total = turn_total + y
            print "Total points:\t", total
            print "Roll:\t", y
            print "Turn total: \t", turn_total
            play = raw_input("Press <Enter> to roll again or 'h' to hold: \n")
            
    return turn_total

def main():
    total = 0
    turn = 1
    while turn <= n:
        print "\n*** TURN %s ***\n" % turn
        turn += 1
        x = play_single_turn(total)
        print "Total points = ", x
        total = total + x
        if total >= g:
            print "\nYOU WIN!"
            print "It took you %s turns to reach %s points." % ((turn-1),g)
            break
        else:
            continue
    else:
        print "\nYOU LOSE!"
        print "You failed to reach %s points in %s turns." % (g,(turn-1))

        
if __name__ == '__main__':
    main()
