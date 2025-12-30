# find ceil and floor from list using binary search
def find_ceil_floor(arr, target):
    low = 0
    high = len(arr) - 1
    ceil = -1
    floor = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return arr[mid], arr[mid]
        elif arr[mid] < target:
            floor = arr[mid]
            low = mid + 1
        else:
            ceil = arr[mid]
            high = mid - 1

    return ceil, floor  # return ceil and floor values

#test case  
arr = [1,2,8,10,10,12,19]
target = 5
print(find_ceil_floor(arr, target))  # Output: (8, 2)
#time complexity: O(log n)
#why? because with each iteration, the search space is halved.
#space complexity: O(1)
#why? because we are using a constant amount of space regardless of the input size.