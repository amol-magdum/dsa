# move zeros from array to the end while maintaining the order of non-zero elements
def move_zeros_to_end(nums):
    n = len(nums)
    
    if n == 1:
        return nums
    i = 0  # pointer for the position to place the next non-zero element
    while i < n:
        if nums[i] == 0:
            break
        i += 1

    if i == n:
        return nums  # no zeros found
    j = i + 1  # pointer to find the next non-zero element
    while j < n:
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    return arr

# test cases
arr = [0, 1, 0, 3, 12]
print(move_zeros_to_end(arr)) # [1, 3, 12, 0, 0]
arr = [1, 0, 2, 0, 0, 3, 4]
print(move_zeros_to_end(arr)) # [1, 2, 3, 4, 0, 0, 0]
arr = [0, 0, 0, 0]
print(move_zeros_to_end(arr)) # [0, 0, 0, 0]
arr = [4, 5, 6]
print(move_zeros_to_end(arr)) # [4, 5, 6]

# time complexity: O(n)
# space complexity: O(1)