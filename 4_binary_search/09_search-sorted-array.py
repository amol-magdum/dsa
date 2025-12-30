# search in sorted rotated array using binary search
def search_rotated_array(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        
        # left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # right half is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
                
    return -1

#test case for search in sorted rotated array
nums = [4,5,6,7,0,1,2]
target = 0
print(search_rotated_array(nums, target))  # Output: 4

#time complexity: O(log n)
#space complexity: O(1)