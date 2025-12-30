# add 3 numbers from linked lists to get 0

def add_three_numbers(nums):
    ans = []
    n = len(nums)
    nums.sort()

    for i in range(n):
        if i != 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = n - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total == 0:
                ans.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
            elif total < 0:
                j += 1
            else:
                k -= 1

    return ans

# test cases
# big list
nums = [-25, -10, -7, -3, 2, 4, 8, 10 , 20, 30, 15, -15, -5, 0, 5, 12, -12, 3, -2, 1]
print(add_three_numbers(nums)) 
# nums = [-1, 0, 1, 2, -1, -4]
# print(add_three_numbers(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
# nums = [0, 1, 1]
# print(add_three_numbers(nums))  # Output: []
# nums = [0, 0, 0]
# print(add_three_numbers(nums))  # Output: [[0, 0, 0]]