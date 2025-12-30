# merge 2 sorted arrays in-place
def merge(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    result=[]
    
    i=0
    j=0
    while i<n and j<m:
        if nums1[i] <= nums2[j]:
            if len(result)==0 or result[-1] != nums1[i]:
                result.append(nums1[i])
                i += 1
        else:
            if len(result)==0 or result[-1] != nums2[j]:
                result.append(nums2[j])
                j += 1

    # If there are remaining elements in nums1, copy them
    while i <n:
        if len(result)==0 or result[-1] != nums1[i]:
            result.append(nums1[i])
            i += 1 
    # If there are remaining elements in nums2, copy them
    while j < m:
        if len(result)==0 or result[-1] != nums2[j]:
            result.append(nums2[j])
            j += 1
    return result
    
# test cases
nums1 = [4,6,7,45,67]
nums2 = [2,4,6,8,9,23,45,78]
print(merge(nums1,nums2))
