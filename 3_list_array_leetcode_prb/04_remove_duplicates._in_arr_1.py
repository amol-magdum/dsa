# remove duplicate from sorted array and return new length
def remove_duplicates(arr):
    if not arr:
        return

    freq_maps = {}
    for num in arr:
        freq_maps[num] = freq_maps.get(num, 0) + 1

    return len(freq_maps)





# test cases
arr = [1, 1, 2]
print(remove_duplicates(arr)) # 2
arr = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(arr)) # 5