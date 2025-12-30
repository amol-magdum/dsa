

nums=[5,23,5,98,3,5,23,5,98,3,45,11,85,65,12,11,45,11,85,65,12,11]

frq_map={}

for i in range(0,len(nums)):
    if nums[i] in frq_map:
        frq_map[nums[i]]+=1
    else:
        frq_map[nums[i]] = 1
print(frq_map)