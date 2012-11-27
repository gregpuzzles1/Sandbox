def computeDistance(height, index, bounces):
    total = 0
    for x in range(bounces):
        total += height
        height *= index
        total += height
    return total

def main():
    while True:
        print "1 Compute the total distance"
        print "2 Quit the program\n"
        command = raw_input("Enter a number: ")
        if not command in ("1", "2"):
            print "Error: unrecognized command"
        elif command == "1":
            height = input("\nEnter the initial height: ")
            index = input("Enter the bounciness index: ")
            bounces = input("Enter the number of bounces: ")
            distance = computeDistance(height, index, bounces)
            print "\nThe distance is", distance, "\n"
        else:
            break

main()

