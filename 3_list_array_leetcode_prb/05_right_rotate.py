# right rotate by one position
def right_rotate(arr):
    if not arr:
        return arr
    n = len(arr)
    LastElement = arr[n-1]
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = LastElement
    return arr

# test cases
arr = [1, 2, 3, 4, 5]
print(right_rotate(arr)) # [5, 1, 2, 3, 4]
arr = [10, 20, 30]
print(right_rotate(arr)) # [30, 10, 20]
arr = [7]
print(right_rotate(arr)) # [7]
arr = []
print(right_rotate(arr)) # []

# time complexity: O(n)
# space complexity: O(1)
# why time complexity is O(n)?
# because we are iterating through the array once to shift elements.
# why space complexity is O(1)?
# because we are not using any extra space that grows with input size.
