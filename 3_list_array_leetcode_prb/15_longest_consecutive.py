# longest consecutive
def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:  # only start counting if 'num' is the start of a sequence
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# test cases
nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [0, -1, 1, 2, -2, 3, 4]
print(longest_consecutive(nums1))  # Output: 4
print(longest_consecutive(nums2))  # Output: 7
# time complexity: O(n)
# space complexity: O(n)