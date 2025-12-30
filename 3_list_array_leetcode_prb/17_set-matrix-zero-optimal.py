# set matrix zeros
def set_matrix_zeros(matrix):
    if not matrix or not matrix[0]:
        return

    r = len(matrix)
    c = len(matrix[0])

    rowtrack = [0 for _ in range(r)]
    coltrack = [0] * c

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                rowtrack[i] = -1
                coltrack[j] = -1

    for i in range(r):
        for j in range(c):
            if rowtrack[i] == -1 or coltrack[j] == -1:
                matrix[i][j] = 0
    return matrix

#test case
matrix1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print(set_matrix_zeros(matrix1))