def separateDigits(n):
    """
    Given an integer n, separate each digit and print.

    Parameters:
    n (int): The integer to be separated into digits.

    Returns:
    list: A list containing the digits of the integer n.
    """
    return [int(digit) for digit in str(n)]


# Example usage:
if __name__ == "__main__":
    number = 7293
    digits = separateDigits(number)
    print(f"The digits in {number} are: {digits}")
    num = number
    while num > 0:
        n = num % 10
        print(n)
        num //= 10
