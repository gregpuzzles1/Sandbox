# Python version = 2.7.2
# Platform = Win32

def ascending(order_square, top_left_number):
    """If order_square > top_left_number"""
    rows_counter = 0
    for rows in range(1, order_square + 1):
        latin_number = top_left_number + (rows - 1)
        if latin_number > order_square:
            latin_number = 1 + rows_counter
            rows_counter += 1
        row_counter = 0
        for row in range(1, order_square + 1):
            print latin_number,
            latin_number += 1
            if latin_number > order_square:
                latin_number = 1 + row_counter
                row_counter += 1
        print

def descending(order_square, top_left_number):
    """If order_square < top_left_number"""
    rows_counter = 1
    for rows in range(1, order_square + 1):
        latin_number = top_left_number - (rows - 1)
        for row in range(1, order_square + 1):
            print latin_number,
            latin_number -= 1
            if latin_number <= (top_left_number - order_square):
                latin_number = top_left_number
        print

def main():
    """Main program"""
    order_square = input('Please input the order of the square: ')
    if order_square > 9:
        order_square = input('Please enter a order between 1 -9: ')
    top_left_number = input('Please input the top left number: ')
    if top_left_number > 9:
        top_left_number = input('Please enter a top left between 1 - 9: ')
    counter = top_left_number
    print "The Latin Square is:"
    if order_square >= top_left_number:
        ascending(order_square, top_left_number)
    else:
        descending(order_square, top_left_number)
        
if __name__ == '__main__':
    main()
