def countOccurance(nums, target):
    n = len(nums)
    count = 0

    for i in range(n):
        if nums[i] == target:
            count += 1
            if nums[i] > target:
                break
    return count

#test case for count occurance
nums = [1,2,2,3,3,3,3,4,5,5,6,6,6,7,7,7,7,7,7,8,8,8,8]
target = 7
print(countOccurance(nums, target))  # Output: 6