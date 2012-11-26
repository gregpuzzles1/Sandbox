#!/usr/bin/env python

def stats(data):
    sum = 0.0
    for value in data:
        sum += value

    mean = sum/len(data)

    sum = 0.0
    for value in data:
        sum += (value - mean)**2

    variance = sum/(len(data) - 1)

    return(mean, variance)

if __name__ == "__main__":
    (m, v) = stats([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print "The mean and variance of the values from 1 to 9 inclusive are ",m, v
