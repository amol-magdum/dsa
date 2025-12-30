# sum of numbers between 1 and n using recursion
def sum_recursive(n):
    if n == 1:
        return 1
    return n + sum_recursive(n - 1) 

if __name__ == "__main__":
    n = 4
    result = sum_recursive(n)
    print(f"Sum of numbers between 1 and {n} is: {result}")
