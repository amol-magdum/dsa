# armstrong number
def is_armstrong_number(num):
    
    num_digits = len(str(num))
    sum_of_powers = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10
    if sum_of_powers == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

# Example usage:
if __name__ == "__main__":
    is_armstrong_number(1535)
    is_armstrong_number(9474)
    
