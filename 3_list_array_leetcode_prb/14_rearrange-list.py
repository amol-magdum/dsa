# re-arrajnge list such that positive number then negative number

def rearrange_list(arr):
    pos = [] # n/2
    neg = [] # n/2
    
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)
    
    result = []
    for i in range(len(pos)):
        result.append(pos[i])
        result.append(neg[i])
    return result

# test cases
arr1 = [33, 2, -5, -1, -4, 3]
arr2 = [-5, 2, -3, 4, -1, 6, -2, 1]
print(rearrange_list(arr1)) # [33, -5, 2, -1, 3, -4]
print(rearrange_list(arr2)) # [2, -5, 4, -3, 6, -1, 1, -2]
#time complexity: O(n)
#space complexity: O(n)