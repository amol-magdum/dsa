# n list has values between 1 to 10
n = [5, 8, 9, 3, 5, 8, 5, 2, 1, 7, 9, 3, 6, 2, 1, 4, 8, 9, 3]
m = [7, 23, 5, 98, 3, 5, 3, 5, 98, 3, 5, 11, 8, 65, 12, 1]

for num in m: # O(m)
    count = 0
    for x in n: # O(n)
        if x == num:
            count += 1
    print(f"{num} : {count}")

# total time complexity = O(m*n) = O(n^2) in worst case when m=n