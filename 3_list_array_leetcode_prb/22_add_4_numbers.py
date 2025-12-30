#[1,1,1,1,3,4,56,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9,0,2,5,6,10,11,12,13,14,15,-10,-11,-12,-13,-14,-15]

def add_4_numbers(nums,target):
    n = len(nums)
    ans = []
    nums.sort()

    for i in range(n):
        if i!= 0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n):
            if j > i+ 1 and nums[j]==nums[j-1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total == target:
                    ans.append([nums[i],nums[j],nums[k],nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k]==nums[k+1]:
                        k += 1
                    while k < l and nums[l]==nums[l-1]:
                        l -= 1
                elif total < target:
                    k += 1
                else:
                    l -= 1

    return ans if ans else ['No combinations found']

# test cases
nums = [1,1,1,1,3,4,56,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
target = 75
print(add_4_numbers(nums,target))