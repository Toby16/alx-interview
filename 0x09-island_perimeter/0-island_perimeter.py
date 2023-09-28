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
    perimeter = 0

    # Define directions (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r < 0 or r >= len(grid)\
                            or c < 0 or c >= len(grid[0])\
                            or grid[r][c] == 0:
                        perimeter += 1

    return perimeter


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
