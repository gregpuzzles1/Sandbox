from __future__ import division
import random

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
        avg = total/n
    else:
        print "\n***GAME SUMMARY***"
        print "With %s turns, you reached %s points." % (n,total)
        print "Average points per turn: %s\n" % avg
    
if __name__ == '__main__':
    main()
