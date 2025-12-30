# search min in rotated sorted array
def find_min(nums: list[int]) -> int:
    n = len(nums)
    low, high = 0, n - 1
    mini = float('inf')

    while low <= high:
        mid = (low+high)//2
        if nums[mid] <= nums[high]:
            mini = min(nums[mid], mini)
            high = mid - 1
        else:
            mini = min(nums[low], mini)
            low = mid + 1
    return mini

# test cases
nums = [4,5,6,7,0,1,2]
print(find_min(nums))  # Output: 0
# time complexity: O(log n)
# space complexity: O(1)