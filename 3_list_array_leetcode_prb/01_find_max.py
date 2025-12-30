# whats leetcode Find Maximum Number in Array # 1299
def max_number(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

arr = [34, 342, -45, 9, 485]
print(max_number(arr)) # 485