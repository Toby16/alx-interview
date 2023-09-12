#!/usr/bin/python3
"""
Rotate 2D Matrix

ALX Interview
"""


def rotate_2d_matrix(matrix):
    """
    function to rotate a 2d matrix in 90 degrees clockwise direction

    Args:
        matrix: 2d matrix (list of lists - n x n)
    """

    # Calculate the number of rows and coli=umns of the matrix
    row = len(matrix)
    column = len(matrix[0])

    # Create new matrix to store the rotated values
    rotated_matrix = [[0] * row for _ in range(column)]

    # Iterate through the original matrix and populate the rotated matrix
    for i in range(row):
        for j in range(column):
            rotated_matrix[j][row - i - 1] = matrix[i][j]

    return rotated_matrix
    # return (matrix)


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix_val = rotate_2d_matrix(matrix)
    # print(rotate_2d_matrix_val)
    for i in rotate_2d_matrix_val:
        print(i)
