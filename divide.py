#!/usr/bin/env python

import sys

def divide(x, y):
    try:
        result = float(x)/float(y)
    except ZeroDivisionError:
        print "division by zero"
    else:
        print "result is ", result
    finally:
        print "executing finally clause"
        print sys.version

def main():
    divide(2, 4)

if __name__ == '__main__':
    main()
