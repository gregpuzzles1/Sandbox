import random
from typing import List, Optional

GRID_SIZE = 81
EMPTY_CELL = '.'


def print_instructions():
    print("=== Interactive Sudoku Game ===")
    print("""
    Instructions:
    1. The program generates a partially filled Sudoku puzzle.
    2. Your goal is to fill in the missing numbers (1-9) to complete the puzzle.
    3. You'll be prompted one by one for each empty cell.
       - Enter a number (1-9) to fill it.
       - Press Enter without typing anything to leave it blank.
    4. After all entries, the program will check if your solution is correct.
    """)


def is_full(grid: List[str]) -> bool:
    return EMPTY_CELL not in grid


def get_trial_cell_index(grid: List[str]) -> Optional[int]:
    for i in range(GRID_SIZE):
        if grid[i] == EMPTY_CELL:
            return i
    return None


def is_legal(trial_val: int, trial_cell_index: int, grid: List[str]) -> bool:
    row = trial_cell_index // 9
    col = trial_cell_index % 9
    square_row = row // 3 * 3
    square_col = col // 3 * 3

    for i in range(9):
        if grid[row * 9 + i] == str(trial_val):
            return False
        if grid[i * 9 + col] == str(trial_val):
            return False

    for i in range(3):
        for j in range(3):
            index = (square_row + i) * 9 + (square_col + j)
            if grid[index] == str(trial_val):
                return False

    return True


def set_cell(trial_val: int, trial_cell_index: int, grid: List[str]):
    grid[trial_cell_index] = str(trial_val)


def clear_cell(trial_cell_index: int, grid: List[str]):
    grid[trial_cell_index] = EMPTY_CELL


def has_solution(grid: List[str]) -> bool:
    if is_full(grid):
        return True

    trial_cell_index = get_trial_cell_index(grid)
    if trial_cell_index is None:
        return False

    for trial_val in range(1, 10):
        if is_legal(trial_val, trial_cell_index, grid):
            set_cell(trial_val, trial_cell_index, grid)
            if has_solution(grid):
                return True
            clear_cell(trial_cell_index, grid)

    return False


def print_grid(grid: List[str]):
    for i in range(9):
        row = grid[i * 9:(i + 1) * 9]
        for j, val in enumerate(row):
            print(val if val != EMPTY_CELL else '.', end=' ')
            if j in [2, 5]:
                print('|', end=' ')
        print()
        if i in [2, 5]:
            print('------+-------+-------')


def generate_full_grid() -> List[str]:
    grid = [EMPTY_CELL] * GRID_SIZE
    _generate_full_grid_helper(grid)
    return grid


def _generate_full_grid_helper(grid: List[str]) -> bool:
    if is_full(grid):
        return True

    trial_cell_index = get_trial_cell_index(grid)
    if trial_cell_index is None:
        return False

    numbers = list(map(str, range(1, 10)))
    random.shuffle(numbers)

    for num in numbers:
        if is_legal(int(num), trial_cell_index, grid):
            set_cell(int(num), trial_cell_index, grid)
            if _generate_full_grid_helper(grid):
                return True
            clear_cell(trial_cell_index, grid)

    return False


def create_puzzle(full_grid: List[str], difficulty: int = 40) -> List[str]:
    puzzle_grid = full_grid[:]
    indices = list(range(GRID_SIZE))
    random.shuffle(indices)
    for i in indices[:difficulty]:
        puzzle_grid[i] = EMPTY_CELL
    return puzzle_grid


def get_user_solution(puzzle_grid: List[str]) -> List[str]:
    user_grid = puzzle_grid[:]
    for i in range(GRID_SIZE):
        if puzzle_grid[i] == EMPTY_CELL:
            row = i // 9 + 1
            col = i % 9 + 1
            while True:
                val = input(f"Enter value for row {row}, column {col} (1-9 or blank): ").strip()
                if val == '':
                    break
                if val in '123456789':
                    if is_legal(int(val), i, user_grid):
                        user_grid[i] = val
                        break
                    else:
                        print(f"Invalid move. {val} at row {row}, column {col} violates Sudoku rules.")
                else:
                    print(f"Invalid input: '{val}'. Please enter a number 1-9 or press Enter to skip.")
    return user_grid


def main():
    print_instructions()

    # Generate and display puzzle
    full_grid = generate_full_grid()
    puzzle_grid = create_puzzle(full_grid, difficulty=40)

    print("\nHere is your puzzle:")
    print_grid(puzzle_grid)

    # Get user input to fill the grid
    user_grid = get_user_solution(puzzle_grid)

    print("\nYour Completed Grid:")
    print_grid(user_grid)

    # Validate solution
    if is_full(user_grid) and all(is_legal(int(user_grid[i]), i, user_grid) for i in range(GRID_SIZE)):
        print("\nCongratulations! You completed the puzzle correctly.")
    else:
        print("\nYour solution is incomplete or incorrect. Keep trying!")


if __name__ == "__main__":
    main()
