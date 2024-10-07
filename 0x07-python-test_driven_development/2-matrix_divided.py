#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix \
                    (list of lists) of integers/floats")
        new_row = []
        row_len = len(matrix[0])
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")
            num = round(num / div, 2)
            new_row.append(num)
        new_matrix.append(new_row)
    return new_matrix
