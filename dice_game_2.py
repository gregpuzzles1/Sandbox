import random

def roll_die():
    """Rolls a 6-sided die and returns the result."""
    return random.randint(1, 6)

def play_single_turn(total):
    """Plays a single turn and returns the score from that turn."""
    play = 'y'
    turn_total = 0

    while play.lower() != 'h':
        roll = roll_die()
        if roll == 1:
            turn_total = 0
            print(f"Total points:\t{total}")
            print(f"Roll:\t{roll}")
            print("Your turn is over!")
            print(f"Turn total:\t{turn_total}")
            input("Press <Enter> to continue... ")
            break
        else:
            turn_total += roll
            print(f"Total points:\t{total}")
            print(f"Roll:\t{roll}")
            print(f"Turn total:\t{turn_total}")
            play = input("Press <Enter> to roll again or 'h' to hold: ")

    return turn_total

def main():
    n = int(input('What is the maximum number of turns?: '))
    total = 0
    turn = 1

    while turn <= n:
        print(f"\n*** TURN {turn} ***\n")
        turn += 1
        points = play_single_turn(total)
        total += points
        avg = total / n

    print("\n*** GAME SUMMARY ***")
    print(f"With {n} turns, you reached {total} points.")
    print(f"Average points per turn: {avg:.2f}\n")

if __name__ == '__main__':
    main()
