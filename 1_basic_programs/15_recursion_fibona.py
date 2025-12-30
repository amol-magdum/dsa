# fibonacci using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Test cases
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(5))  # 5
print(fibonacci(10)) # 55
print(fibonacci(15)) # 610