
def recursion_reverse_aray(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    recursion_reverse_aray(arr, start + 1, end - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    recursion_reverse_aray(arr, 0, len(arr) - 1)
    print("Reversed array:", arr)