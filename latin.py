def word_index(x):
    """ Returns index in word where stem starts """
    counter = 0
    for i in x:
        counter += 1
        if (i == "a" or i == "e" or i == "i" or i == "o" \
           or i == "u") and counter != 1:
            return counter - 1
        else:
            pass
        if counter == len(x):
            return 10000

def reverse_word(x, y):
    """ Reverse prefix and stem of the word x """
    yy = x[:y]
    zz = x[y:]
   
    if (y == 10000) and ((yy != "a") and (yy != "e") and (yy != "i") and \
                         (yy != "o") and (yy != "u")):
        print "Pig Latin: ", x + 'ay'
        return
    elif x[:2] == "qu":
        yyy = x[:2]
        zzz = x[2:]
        xyz = zzz + yyy + 'ay'
        print "Pig Latin: ", xyz
        return
    elif ((yy == "a") or (yy == "e") or (yy == "i") or \
          (yy == "o") or (yy == "u")):
        y2 = yy + 'yay'
        print "Pig Latin: ", y2
        return
    else:
        yz = zz + yy + 'ay'
        print "Pig Latin: ", yz

def main():
    """ Main program """
    x = raw_input("English: ")
    y = word_index(x)
    yy = reverse_word(x, y)

if __name__ == '__main__':
    main()
