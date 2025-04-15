def is_vowel(c):
    '''Returns True if the character c is a vowel.'''
    return c.lower() in 'aeiou'

def is_consonant(c):
    '''Returns True if the character c is a consonant.'''
    return c.isalpha() and not is_vowel(c)

def is_digit(c):
    '''Returns True if the character c is a digit.'''
    return c.isdigit()

def is_whitespace(c):
    '''Returns True if the character c is a whitespace character.'''
    return c in ' \t\n\r'

def collect_statistics(filename):
    '''Collects the relevant statistics from the file.'''
    num_lines = 0
    consonants = 0
    vowels = 0
    digits = 0
    whitespace = 0
    longest_line_length = 0
    total_characters = 0

    for line in filename:
        num_lines += 1
        line_length = len(line)
        total_characters += line_length

        if line_length > longest_line_length:
            longest_line_length = line_length

        for char in line:
            if is_vowel(char):
                vowels += 1
            elif is_consonant(char):
                consonants += 1
            elif is_digit(char):
                digits += 1
            elif is_whitespace(char):
                whitespace += 1

    print_statistics(num_lines, total_characters, consonants, vowels, digits, whitespace, longest_line_length)

def print_statistics(lines, total_characters, consonants, vowels, digits, whitespace, longest_line):
    '''Prints the file statistics.'''
    print("Number of Lines:", lines)
    print("Total Characters:", total_characters)
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Digits:", digits)
    print("Whitespace Characters:", whitespace)
    print("Length of Longest Line:", longest_line)

def main():
    '''Prompts the user for a filename and gathers statistics.'''
    filename = input('Please enter the name of the file: ')
    try:
        with open(filename, 'r') as file:
            print('\n**** FILE SUMMARY ****\n')
            collect_statistics(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

main()
