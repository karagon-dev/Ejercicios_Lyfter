import math

numbers = [1, 4, 6, 7, 13, 9, 67]

def is_prime(entered_number):
    if entered_number < 2:
        return False
    square_root = math.floor(entered_number ** 0.5)
    for number in range(2, square_root + 1):
        if (entered_number % number) == 0:
            return False
    return True


def keep_prime_numbers(my_numbers):
    prime_numbers = []
    for index in range(0, len(my_numbers), 1):
        if is_prime(my_numbers[index]):
            prime_numbers.append(my_numbers[index])
    return prime_numbers

print(keep_prime_numbers(numbers))