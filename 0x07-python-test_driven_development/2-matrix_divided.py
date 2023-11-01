
def matrix_divided(matrix, div):
    new_list = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

        for x in matrix[i]:
            if not isinstance(x, (int, float)):
                raise TypeError(
                 "matrix must be a matrix (list of lists) of integers/floats")
            new_list.append(round(x / div, 2))
    return new_list
