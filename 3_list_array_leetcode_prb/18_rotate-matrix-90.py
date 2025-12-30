# roate matrix by 90 degree clockwise without using extra space
def rotate_matrix(matrix):
    n = len(matrix)
    # transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    

#test cases matrix 4*4
matrix1 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
rotate_matrix(matrix1)
for row in matrix1:
    row.reverse()
print(matrix1)