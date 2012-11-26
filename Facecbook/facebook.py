# Python version = 2.7.2
# Platform = win32

import sys

# N = The number of discs where 1 <= N <= 8
# K = The number of pegs where 3 <= K <= 5

def input00():
    f = open('input01.txt', 'r')
    print "f= ", f
    line_counter = 1
    initial = []
    final = []
    for line in f:
        line = line.strip().replace(' ', '')
        print "line = ", line
        if line_counter == 1:
            N = line[0]
            K = line[1]
        elif line_counter == 2:
            for number in line:
                initial.append(number)
                print "initial = ", number
        elif line_counter == 3:
            for number in line:
                final.append(number)
                print "final = ", number
        else:
            print "error message"
        line_counter += 1
    f.close()
    print "f = ", f
    return initial, final

def move(initial, final):
    print initial
    print final
    print initial.pop(0)
    for i in final:
        for r in initial:
            if r == i:
                pass
    

def main():
    sample_in = input00()
    move(sample_in[0], sample_in[1])
    
if __name__ == '__main__':
    main()
