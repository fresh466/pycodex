"""
The program takes square size from command-line arguments, and generates a magic square of that size. It then prints it out as a grid of numbers.
"""
import sys

argc = len(sys.argv)

def main():
    """
    The main function.
    """
    if argc != 2:
        print("Usage: python magic_square.py <size>")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("Size must be an integer.")
        sys.exit(1)
    if size < 3:
        print("Size must be at least 3.")
        sys.exit(1)
    if size % 2 == 0:
        print("Size must be odd.")
        sys.exit(1)
    square = generate_magic_square(size)
    print_square(square)

def generate_magic_square(size):
    """
    Generates a magic square of the given size.
    """
    square = [[0 for i in range(size)] for j in range(size)]
    row = 0
    column = size // 2
    square[row][column] = 1
    for i in range(2, size * size + 1):
        new_row = (row - 1) % size
        new_column = (column + 1) % size
        if square[new_row][new_column] != 0:
            new_row = (row + 1) % size
            new_column = column
        square[new_row][new_column] = i
        row = new_row
        column = new_column
    return square

def print_square(square):
    """
    Prints the square as a grid of numbers.
    """
    for row in square:
        for number in row:
            print(number, end="\t")
        print()

if __name__ == "__main__":
    main()