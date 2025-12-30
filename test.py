# return index or -1 if not found
def find_index(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1


# Example usage:
nums = [4, 2, 3, 5, 2]
target = 3
result = find_index(nums, target)
print(f"Index of {target} in the list is: {result}")  # Output should be 2
