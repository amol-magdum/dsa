# find second largest element in an array
def second_largest(arr):

    largest = float('-inf')
    second_largest = float('-inf')

    n = len(arr)
    for i in range(0,n):
        largest = max(largest, arr[i])

    for i in range(0,n):
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    return None if second_largest == float('-inf') else second_largest

# test the function
arr = [12, 35, 1, 10, 34, 10]
print("The second largest element is:", second_largest(arr))

arr = [10, 5, 10]
print("The second largest element is:", second_largest(arr))

arr = [10, 10, 10]
print("The second largest element is:", second_largest(arr))

arr = [5]
print("The second largest element is:", second_largest(arr))

# time complexity: O(n)
# space complexity: O(1)