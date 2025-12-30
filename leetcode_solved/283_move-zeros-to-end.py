# move zeros from array to the end while maintaining the order of non-zero elements
def move_zeros_to_end(arr):
    n = len(arr)
    count = 0  # count of non-zero elements

    # Traverse the array. If element is non-zero, then
    # replace the element at index 'count' with this element
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been shifted to
    # front and 'count' is set as index of first 0.
    # Make all elements 0 from count to end.
    while count < n:
        arr[count] = 0
        count += 1

    return arr

# test cases
arr = [0, 1, 0, 3, 12]
print(move_zeros_to_end(arr)) # [1, 3, 12, 0, 0]
arr = [1, 0, 2, 0, 0, 3, 4]
print(move_zeros_to_end(arr)) # [1, 2, 3, 4, 0, 0, 0]
arr = [0, 0, 0, 0]
print(move_zeros_to_end(arr)) # [0, 0, 0, 0]
arr = [4, 5, 6]
print(move_zeros_to_end(arr)) # [4, 5, 6]

# time complexity: O(n)
# space complexity: O(1) 

