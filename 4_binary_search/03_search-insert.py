# LEETCODE 35: Search Insert Position
# https://leetcode.com/problems/search-insert-position/
def search_insert(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low  # target not found, return the insert position

# test case
arr = [1,3,5,6]
print(search_insert(arr,5))  # Output: 2
#time complexity: O(log n)
#why? because with each iteration, the search space is halved.
#space complexity: O(1)
#why? because we are using a constant amount of space regardless of the input size.
