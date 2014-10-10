def sum_of_digits(number):
    digits = str(int(number))
    print(digits)
    sum = 0
    for digit in digits:
        if digit.isdigit():
            sum += int(digit)
    return sum


def main():
    print(sum_of_digits('-010325132435356'))


if __name__ == '__main__':
    main()
