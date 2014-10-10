import math


def sum_of_divisors(n):
    divisors = find_divisors(n)
    sum = 0
    for x in divisors:
        sum += x
    return sum


def find_divisors(n):
    divisors = []
    divisors.append(1)
    divisors.append(n)
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            divisors.append(x)
            if (x != int(n / x)):
                divisors.append(int(n / x))
    return divisors


def main():
    print(sum_of_divisors(1000))


if __name__ == '__main__':
    main()
