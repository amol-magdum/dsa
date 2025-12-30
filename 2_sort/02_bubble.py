# bubble sort [adjacent swaps] and calculate time complexity and space complexity
# largest element bubbles to the end in each pass

# def buuble_sort(arr):
#     n = len(arr) 
#     is_sorted = False # optimization to stop if already sorted
#     for i in range (n-1):  
#         for j in range (i+1, n):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#                 is_sorted = True
#         if not is_sorted: 
#             return
#     return arr

def buuble_sort(arr):
    n = len(arr)
    for i in range(n-2, 0, -1):
        is_sorted = False # optimization to stop if already sorted
        for j in range(0, i+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = True
        if not is_sorted: 
            return arr
    return arr
# Test cases
print(buuble_sort([64, 25, 12, 2, 11]))  # [11, 12, 22, 25, 64]
print(buuble_sort([5, 3,  8, -6, 2]))        # [2, 3, 5, 6, 8]
print(buuble_sort([]))                     # []

# time complexity: O(n^2) in all cases (best, average, worst)
# space complexity: O(1) (in-place sorting)