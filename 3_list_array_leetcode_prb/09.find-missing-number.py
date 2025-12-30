# find missing number in array
def missingNumber(nums):
    n = len(nums)
    for i in range(n+1):
        if i not in nums:
            return i

# test cases
arr1 = [3,0,1]
arr2 = [0,1]
arr3 = [9,6,4,2,3,5,7,0,1]
print(missingNumber(arr1)) # 2
print(missingNumber(arr2)) # 2
print(missingNumber(arr3)) # 8

# time complexity: O(n^2) due to the 'in' operation inside the loop
# space complexity: O(1)