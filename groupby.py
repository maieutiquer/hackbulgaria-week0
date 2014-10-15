from collections import defaultdict


def groupby(func, seq):
    dictionary = defaultdict(list)
    for x in seq:
        if func(x):
            dictionary[func(x)].append(x)
        else:
            dictionary[func(x)].append(x)
    return dictionary.items()


def main():
    print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))


if __name__ == '__main__':
    main()
