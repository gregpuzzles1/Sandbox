import random

def roll_die():
    """Roll a 6-sided die and return the result."""
    return random.randint(1, 6)

def play_single_turn(total):
    """Play a single turn and return the points earned in that turn."""
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
    print("Welcome to the Dice Game!")
    g = int(input('How many points to win?: '))
    n = int(input('What is the maximum number of turns?: '))

    total = 0
    turn = 1

    while turn <= n:
        print(f"\n*** TURN {turn} ***\n")
        turn += 1
        turn_points = play_single_turn(total)
        total += turn_points
        print(f"Total points = {total}")

        if total >= g:
            print("\n🎉 YOU WIN!")
            print(f"It took you {turn - 1} turns to reach {g} points.")
            break
    else:
        print("\n😞 YOU LOSE!")
        print(f"You failed to reach {g} points in {n} turns.")

if __name__ == '__main__':
    main()
