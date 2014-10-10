from sum_of_divisors import find_divisors


def is_prime(n):
    if n <= 1:
        return False
    return (len(find_divisors(n)) == 2)


def main():
    print(is_prime(-10))


if __name__ == '__main__':
    main()
