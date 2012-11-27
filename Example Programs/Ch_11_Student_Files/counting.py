"""
File: counting.py
Prints the the number of iterations for problem sizes 
that double, using a nested loop.
"""

problemSize = 1000
print "%12s%15s" % ("Problem Size", "Iterations")
for count in xrange(5):
    number = 0

    # The start of the algorithm
    work = 1
    for j in xrange(problemSize):
        for k in xrange(problemSize):
            number += 1
            work += 1
            work -= 1
   # The end of the algorithm
    
    print "%12d%15d" % (problemSize, number)
    problemSize *= 2
