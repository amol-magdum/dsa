n = [5, 8, 9, 3, 5, 8, 5, 2, 1, 7, 9, 3, 6, 2, 1, 4, 8, 9, 3]
m = [7, 23, 5, 98, 3, 5, 3, 5, 98, 3, 5, 11, 8, 65, 12, 1]

hash_map = [0]*11  # since values are between 1 to 10 #space complexity O(1)

for num in n:  # O(n)
    hash_map[num] += 1

for num in m:  # O(m)
    if num < 1 or num > 10:
        print(f"{num} : 0")
    else:
        print(f"{num} : {hash_map[num]}")

# total time complexity = O(n + m) = O(n) in worst case when m=n