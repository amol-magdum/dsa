
def factorial_r(n):
    if n==1:
        return 1
    return n * factorial_r(n-1)

if __name__ == "__main__":
    n = 5
    result = factorial_r(n) # 120
    print(f"Factorial of {n} is: {result}")