# count target occurance in a sorted array using binary search
def lower_bound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    lb = -1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1    
    return lb

def upper_bound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    ub = -1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] <= target:
            ub = mid
            low = mid + 1
        else:
            high = mid - 1    
            
    return ub

# leetcode 34: count the occurence of target in sorted array
def count_occurance(nums, target):
    first = lower_bound(nums, target)
    last = upper_bound(nums, target)
    if first == -1 or last == -1:
        return 0
    return last - first + 1 

#test case for count occurance
nums = [1,2,2,3,3,3,3,4,5,5,6,6,6,7,7,7,7,7,7,8,8,8,8]
target = 7
print(count_occurance(nums, target))  # Output: 6