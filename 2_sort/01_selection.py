# leetcode Selection Sort Algorithm number # 1475
# selection sort and calculate time complexity
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range (i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Test cases
print(selection_sort([64, 25, 12, 22, 11]))  # [11, 12, 22, 25, 64]
print(selection_sort([5, 3, 8, 6, 2]))        # [2, 3, 5, 6, 8]
print(selection_sort([]))                     # []

# time complexity: O(n^2) in all cases (best, average, worst)
# space complexity: O(1) (in-place sorting)
#explain time complexity
# The time complexity of selection sort is O(n^2) because it consists of two nested
# loops. The outer loop runs n times (where n is the number of elements in the array),
# and for each iteration of the outer loop, the inner loop runs up to n times in the worst case.
# Therefore, the total number of comparisons made is proportional to n * n, which simplifies to O(n^2).