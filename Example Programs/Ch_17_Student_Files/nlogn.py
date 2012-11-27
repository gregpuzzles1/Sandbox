from math import log

n = 512
for x in xrange(1, 10, 1):
    print "%8d%12d%16d" % (n, n * log(n, 2), n ** 2)
    n *= 4
