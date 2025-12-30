# remove duplicate from sorted array and return new length
def remove_duplicates(arr):
    if not arr:
        return
    n = len(arr)
    i =0
    j = i + 1
    while j < n:
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
        j += 1
    return arr
# test cases
arr = [1, 1, 2]
print(remove_duplicates(arr)) # 2
arr = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(arr)) # 5