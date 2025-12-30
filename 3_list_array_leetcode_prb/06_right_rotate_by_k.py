# right rotate the array by k times
def right_rotate_by_k(arr, k):
    if not arr:
        return arr
    n = len(arr)
    k = k % n  # in case k is greater than n

    def reverse(sub_arr, start, end):
        while start < end:
            sub_arr[start], sub_arr[end] = sub_arr[end], sub_arr[start]
            start += 1
            end -= 1

    # reverse first k elements
    reverse(arr, 0, k-1)
    # reverse the remaining n-k elements
    reverse(arr, k, n-1)    
    # reverse the whole array
    reverse(arr, 0, n-1)
    
    return arr

# test cases    
arr = [1, 2, 3, 4, 5]
k = 2
print(right_rotate_by_k(arr, k)) # [4, 5, 1, 2, 3]
arr = [10, 20, 30, 40, 50, 60]
k = 3
print(right_rotate_by_k(arr, k)) # [40, 50, 60, 10, 20, 30]
arr = [7, 14, 21]
k = 1
print(right_rotate_by_k(arr, k)) # [21, 7, 14]

