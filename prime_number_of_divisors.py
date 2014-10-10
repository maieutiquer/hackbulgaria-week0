from sum_of_divisors import find_divisors
from is_prime import is_prime


def prime_number_of_divisors(n):
    if n == 1:
        return True
    elif n < 1:
        return False
    number_of_divisors = len(find_divisors(n))
    return is_prime(number_of_divisors)


def main():
    print(prime_number_of_divisors(9))


if __name__ == '__main__':
    main()
