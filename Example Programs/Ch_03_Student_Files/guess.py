import random

smaller = input("Enter the smaller number: ")
larger = input("Enter the larger number: ")
myNumber = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    userNumber = input("Enter your guess: ")
    if userNumber < myNumber:
        print "Too small"
    elif userNumber > myNumber:
        print "Too large"
    else:
        print "You've got it in", count, "tries!"
        break
