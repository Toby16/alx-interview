#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Function to return the perimeter of the island described in grid

    Args:
        grid [2d list] - A list of list of integers
                         0 represents water
                         1 represents land
                         Each cell is square, with a side length of 1
                         Cells are connected horizontally/vertically -
                          (not diagonally)
                         grid is rectangular -
                          with its width and height not exceeding 100

            * The grid is completely surrounded by water
            * There is only one island (or nothing)
            * The island doesn’t have “lakes” -
                (ie. water inside that isn’t connected to the water
                surrounding the island)
    """
    """
    a = 0
    while a < len(grid):
        print("i[{}] = {}".format(a, grid[a]))
        a += 1

    print()

    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            # Determine the position of each cells
            if grid[i][j] == 1:
                print("i[{}] * j[{}] = {}".format(i, j, grid[i][j]))
            j += 1
        i += 1


    print()
    """

    # Sum horizontally
    horizontal_sum = [sum(row) for row in grid]

    # Sum vertically
    vertical_sum = sum(horizontal_sum) + 1

    # print(horizontal_sum)  # Output: [3, 7]
    # print(vertical_sum)    # Output: 10
    # return vertical_sum
    perimeter_val = vertical_sum * 2

    return perimeter_val


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    # island_perimeter(grid)
