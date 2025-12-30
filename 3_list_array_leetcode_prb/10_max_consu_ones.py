# find max consutive ones in binary array
def findMaxConsecutiveOnes(nums):
    max_count = 0
    count = 0

    for i in range (0, len(nums)):
        if nums[i] == 1:
            count += 1
        
        else:
            max_count = max(max_count, count)
            count = 0
    
    return max(max_count, count)

# test cases
arr1 = [1,1,0,1,1,1]
arr2 = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(arr1)) # 3
print(findMaxConsecutiveOnes(arr2)) # 2

# time complexity: O(n)
# space complexity: O(1)