# leetcode 43: find the first and last occurenace of target
def first_last_occurance(nums, target):
    n = len(nums)
    first = -1
    last = -1

    for i in range (n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]
            


#test case for first and last occurance
nums = [1,2,2,3,3,3,3,4,5,5,6,6,6,7,7,7,7,7,7,8,8,8,8]
target = 7
print(first_last_occurance(nums, target))  # Output: [13, 18]

#time complexity: O(n)
#space complexity: O(1)

