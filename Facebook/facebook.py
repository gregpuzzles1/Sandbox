def read_input_file(filename: str):
    """
    Reads the input file and returns initial and final states.
    Expected format:
    Line 1: Two digits, N (number of discs) and K (number of pegs)
    Line 2: Initial configuration of discs
    Line 3: Final configuration of discs
    """
    initial = []
    final = []

    with open(filename, 'r') as f:
        lines = f.readlines()

    if len(lines) < 3:
        raise ValueError("Input file must have at least 3 lines.")

    # Process line 1
    line1 = lines[0].strip().replace(' ', '')
    N = int(line1[0])
    K = int(line1[1])
    print(f"N (discs): {N}, K (pegs): {K}")

    # Process line 2: Initial configuration
    line2 = lines[1].strip().replace(' ', '')
    initial = list(line2)
    print(f"Initial configuration: {initial}")

    # Process line 3: Final configuration
    line3 = lines[2].strip().replace(' ', '')
    final = list(line3)
    print(f"Final configuration: {final}")

    return N, K, initial, final


def move_discs(initial: list, final: list):
    """
    Sample move logic: prints out moves needed to go from initial to final.
    """
    print(f"Initial: {initial}")
    print(f"Final: {final}")

    while initial:
        disc = initial.pop(0)
        print(f"Moving disc: {disc}")
        # This is placeholder logic. Insert real disc moving logic here.
        for i in final:
            if disc == i:
                print(f"Disc {disc} matches with final position {i}")
                break


def main():
    filename = 'input01.txt'
    try:
        N, K, initial, final = read_input_file(filename)
        move_discs(initial, final)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
