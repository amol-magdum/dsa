# print matrix in spiral order
def print_spiral(matrix):
    if not matrix or not matrix[0]:
        return []
    
    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range (left, right +1):
            result.append(matrix[top][i]) 
        top += 1
        for i in range (top, bottom +1):
            result.append(matrix[i][right])
        right -= 1
            
        if top <= bottom:
            for i in range (right, left -1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range (bottom, top -1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

# test cases
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(print_spiral(matrix1))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(print_spiral(matrix2))  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]