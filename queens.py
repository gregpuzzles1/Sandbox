BOARD_SIZE = 8

class BailOut(Exception):
    """Custom exception used to backtrack during invalid placements."""
    pass

def validate(queens):
    """
    Validates that the last queen added does not conflict diagonally or vertically
    with any of the previously placed queens.
    """
    col = queens[-1]
    left = right = col
    for row_queen in reversed(queens[:-1]):
        left -= 1
        right += 1
        if row_queen in (left, col, right):
            raise BailOut

def add_queen(queens):
    """
    Attempts to place a queen in the next row. If all queens are placed,
    returns the list of columns for each row.
    """
    for column in range(BOARD_SIZE):
        next_queens = queens + [column]
        try:
            validate(next_queens)
            if len(next_queens) == BOARD_SIZE:
                return next_queens
            else:
                return add_queen(next_queens)
        except BailOut:
            continue
    raise BailOut

# Solve the problem
queens = add_queen([])

# Output the result
print(queens)
print("\n".join(". " * q + "Q " + ". " * (BOARD_SIZE - q - 1) for q in queens))
