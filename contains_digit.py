def contains_digit(number, digit):
    stringRepresentationOfNumber = str(number)
    return str(digit) in stringRepresentationOfNumber


def main():
    print(contains_digit(111112, 3))


if __name__ == '__main__':
    main()
