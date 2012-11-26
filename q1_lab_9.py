def is_vowel(c):
    ''' Returns True if the character c is a vowel.  Otherwise, returns False.'''
    pass

def is_consonant(c):
    ''' Returns True if the character c is a consonant.  Otherwise, returns False.'''
    for line in c:
        
        print line

def is_digit(c):
    ''' Returns True if the character c is a digit.  Otherwise, returns False.'''
    pass

def is_whitespace(c):
    ''' Returns True if the character c is a whitespace character.  Otherwise, returns False.'''
    pass

def collect_statistics(filename):
    ''' Collects the relevant statistics from the file specified by the string filename. '''
    xy = 0
    num_lines = 0
    consonants = 0
    vowels = 0
    digits = 0
    whitespace = 0
    longest_line_length = 0
    total_characters = 0
    for line in filename:
        num_lines += 1
        xy = len(line)
        if longest_line_length < xy:
            longest_line_length = xy
    is_consonant(filename)
    
    print_statistics(num_lines, total_characters, consonants, vowels, digits, 
                     whitespace, longest_line_length)


def print_statistics(lines, total_characters, consonants, vowels, digits, 
                     whitespace, longest_line):
    ''' Prints the file statistics.'''
    print "Number of Lines: ", lines
    print "Length of Longest Line: :", longest_line

def main():
    ''' Prompts the user for a filename. Afterwards, calls the function collect_statistics
        to gather the statistics.
    '''
    c = open(raw_input('Please enter the name of the file: '))
    print '\n****FILE SUMMARY****\n'
    x = collect_statistics(c)
main()

