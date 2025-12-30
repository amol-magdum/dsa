# find index from list using binary search with recursion

def find_index_recursive(arr, target, low, high):
    low = 0
    high = len(arr) -1
    if low > high:
        return -1  # Base case: target not found

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return find_index_recursive(arr, target, mid + 1, high)
    else:
        return find_index_recursive(arr, target, low, mid - 1)
    
# wrapper function to initiate recursion
def find_index(arr, target):
    return find_index_recursive(arr, target, 0, len(arr) - 1)
# test case
arr = [1,2,3,4,5,6,7,8,9,10]
print(find_index(arr,7))  # Output: 6

#time complexity: O(log n)
#why? because with each iteration, the search space is halved.
#space complexity: O(log n)
#why? because of the recursive call stack, which can go as deep as log n in the worst case.
