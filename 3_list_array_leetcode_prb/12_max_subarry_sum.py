# find max subarry sum
def max_subarray_sum(nums):
    n = len(nums)
    max_sum = float('-inf')

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum

# test cases
arr1 = [-2,1,-3,4,-1,2,1,-5,4]
arr2 = [1]
arr3 = [5,4,-1,7,8]
print(max_subarray_sum(arr1)) # 6
print(max_subarray_sum(arr2)) # 1
print(max_subarray_sum(arr3)) # 23

# time complexity: O(n^2)
# space complexity: O(1)

#optimal solution
def max_subarray_sum_optimal(nums):
    n = len(nums)
    max_sum = nums['-inf']
    total = 0

    for i in range(0, n):
        total = total + nums[i]
        max_sum = max(max_sum, total)
        if total < 0:
            total = 0

    return max_sum

# test cases
arr1 = [-2,1,-3,4,-1,2,1,-5,4]
arr2 = [1]
arr3 = [5,4,-1,7,8]
print(max_subarray_sum(arr1)) # 6
print(max_subarray_sum(arr2)) # 1
print(max_subarray_sum(arr3)) # 23