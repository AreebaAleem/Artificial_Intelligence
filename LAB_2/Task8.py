def matrix_multiplication(matrix1, matrix2):

    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

matrix1 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]
matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

result_matrix = matrix_multiplication(matrix1, matrix2)

for row in result_matrix:
    print(row)