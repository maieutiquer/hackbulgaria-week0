def contains_digits(number, digits):
    stringRepresentationOfNumber = str(number)
    for x in digits:
        if str(x) not in stringRepresentationOfNumber:
            return False
    return True


def main():
    print(contains_digits(456, []))


if __name__ == '__main__':
    main()
