# what is palindrome?
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

def is_palindrome(s):
    # using recursion
    # s = ''.join(c.lower() for c in s if c.isalnum())  # Normalize the string
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Test cases
print(is_palindrome("ABCD"))  # False
print(is_palindrome("ABCBA"))  # True
print(is_palindrome(""))  # True