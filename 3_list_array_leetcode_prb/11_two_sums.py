# return index of 2 numbers such that they add up to a specific target
def twoSum(nums, target):
    freq = {}

    for i in range (0, len(nums)):
        complement = target - nums[i]
        if complement in freq:
            return [freq[complement], i]
        freq[nums[i]] = i
    return []

# time complexity: O(n)
# space complexity: O(n)


# test cases
arr1 = [2,7,11,15]
arr2 = [3,2,4]
arr3 = [3,3]
print(twoSum(arr1, 9)) # [0, 1]
print(twoSum(arr2, 6)) # [1, 2]
print(twoSum(arr3, 6)) # [0, 1]

# another approach using brute force
def twoSumBruteForce(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# test cases
print(twoSumBruteForce(arr1, 9)) # [0, 1]

# time complexity: O(n^2)
# space complexity: O(1)