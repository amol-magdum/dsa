# check if number is palindrome or not
# 12321 -> palindrome
# 1232 -> not palindrome

def is_palindrome(n: int) -> bool:
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original == reversed_num

if __name__ == "__main__":
    n = 1232
    if is_palindrome(n):
        print(f"{n} is a palindrome")
    else:
        print(f"{n} is not a palindrome")   

# time complexity: O(d) where d is number of digits in n
# space complexity: O(1)