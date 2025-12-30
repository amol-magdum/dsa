# find missing number in array
def missingNumber(nums):
    n = len(nums)
    freq = {}

    for i in range (0, n + 1):
        freq[i] = 0

    for num in nums:
        freq[num] = 1

    for k, v in freq.items():
        if v == 0:
            return k




# test cases
arr1 = [3,0,1]
arr2 = [0,1]
arr3 = [9,6,4,2,3,5,7,0,1]
print(missingNumber(arr1)) # 2
print(missingNumber(arr2)) # 2
print(missingNumber(arr3)) # 8

# time complexity: O(n)
# space complexity: O(n)