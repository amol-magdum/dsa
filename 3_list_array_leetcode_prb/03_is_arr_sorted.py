# is array sorted in non-decreasing order
def is_array_sorted(arr):
    n = len(arr)
    for i in range(0, n - 1):
        if arr[i] > arr[i + 1]:
            return False    
    return True

#test
arr = [1, 2, 2, 3, 4, 5]
print(is_array_sorted(arr)) # True  
arr = [1, 3, 2, 4, 5]
print(is_array_sorted(arr)) # False
arr = [5, 4, 3, 2, 1]
print(is_array_sorted(arr)) # False







