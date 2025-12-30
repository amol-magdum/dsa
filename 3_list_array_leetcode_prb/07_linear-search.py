
def linear_search(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1

# test cases
arr = [4, 2, 3, 5, 1]
print(linear_search(arr, 5)) # 3
print(linear_search(arr, 1)) # 4
print(linear_search(arr, 6)) # -1
