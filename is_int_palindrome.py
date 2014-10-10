import math


def is_int_palindrome(n):
    number = str(n)
    for x in range(0, int(math.floor(len(number) / 2.0))):
        if number[x] != number[len(number) - 1 - x]:
            return False
    return True


def main():
    print(is_int_palindrome(1233221))


if __name__ == '__main__':
    main()
