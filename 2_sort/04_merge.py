
def merge_array(left, right):
    result = []
    i, j = 0 , 0
    n, m = len(left), len(right)
    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else: # left[i] >= right[j]
            result.append(right[j])
            j += 1
    
    # Append remaining elements
    if i < n:
        result.extend(left[i:])
    if j < m:
        result.extend(right[j:])

    return result

def merge_sort(arr):
    if len(arr) <=1 :
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge_array(left, right)

# Test cases
print(merge_sort([38, 27, 43, 3, 9, 82, 10])) # [3, 9, 10, 27, 38, 43, 82]
print(merge_sort([])) # []  
print(merge_sort([1])) # [1]
print(merge_sort([5, 4, 3, 2, 1])) # [1, 2, 3, 4, 5]

# time complexity: O(n log n) where n is the length of the array
# space complexity: O(n) for the temporary arrays used in merging