from exceptions import StopIteration

lyst = [10, 20, 30]

iterator = iter(lyst)

while True:
    try:
        print iterator.next()
    except StopIteration:
        break
