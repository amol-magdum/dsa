# find lower bound index in list using binary search
def find_lower_bound(arr, target):
    low = 0
    high = len(arr)
    lb = -1
    ub = -1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            lb = mid
            high = mid
        else:
            ub = mid
            low = mid + 1
    return ub
# test case
arr = [1,2,4,4,5,6,7,7,8,8,8,8,8,8,9,10]
print(find_lower_bound(arr,8))  # Output: 2