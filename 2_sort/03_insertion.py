# calculate time and space complexity
# insertion sort [shifting elements] and calculate time complexity and space complexity
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort([5, 2, 9, 1, 5, 6]))

# time complexity: O(n^2) in average and worst case, O(n) in best case (when array is already sorted)
# space complexity: O(1) (in-place sorting)
# why time complexity is n^2 in average and worst case?
# because for each element, we may have to compare it with all the previous elements in the array
# why time complexity is O(n) in best case? 
# because we only need to make one pass through the array, and no shifting is needed 