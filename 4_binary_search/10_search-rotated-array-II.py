# leetcode 81. Search in Rotated Sorted Array II
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

def search(nums: list[int], target: int) -> int:
    n = len(nums)
    low, high = 0, n-1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        # handle duplicates
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
        # left half is sorted
        elif nums[low] <= nums[mid]:
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
    return False

# test cases
nums = [5,6,7,0,1,2,3,4]
target = 4
print(search(nums, target))  # Output: 7

# time complexity: O(log n)
# space complexity: O(1)
