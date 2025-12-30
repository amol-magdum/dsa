def countNumberInDigits(n: int) -> int:
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

if __name__ == "__main__":
    n = 1234567
    print(f"Count of numbers from 1 to {n} in digits is: {countNumberInDigits(n)}") 