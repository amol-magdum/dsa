# find index from list using binary search
def find_index(arr, target):
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

    return -1  # target not found



# test case
arr = [1,2,3,4,5,6,7,8,9,10]
print(find_index(arr,1))  # Output: 6

#time complexity: O(log n)
#why? because with each iteration, the search space is halved.  

#space complexity: O(1) 
#why? because we are using a constant amount of space regardless of the input size.