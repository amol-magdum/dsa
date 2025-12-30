

nums=[5,23,5,98,3,5,23,5,98,3,45,11,85,65,12,11,45,11,85,65,12,11]

n = len(nums)
hash_map={}

for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1

print(hash_map)