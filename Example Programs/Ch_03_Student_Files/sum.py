sum = 0.0
data = raw_input("Enter a number: ")
while data != "":
    number = float(data)
    sum += number
    data = raw_input("Enter the next number: ")
print "The sum is", sum
