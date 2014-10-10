import math


def is_number_balanced(n):
    nAsString = str(n)
    leftPart = ""
    for x in (0, math.floor(len(nAsString) / 2.0)):
        leftPart += x
    rightPart = ""
    for x in (math.ceil(len(nAsString) / 2.0), len(nAsString)):
        rightPart += x
    print(rightPart + rightPart)


def main():
    print(is_number_balanced(9))


if __name__ == '__main__':
    main()
