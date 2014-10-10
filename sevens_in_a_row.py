def sevens_in_a_row(arr, n):
    sevens = 0
    for i in arr:
        if i == 7:
            sevens += 1
            if sevens == n:
                return True
        else:
            sevens = 0
    return False


def main():
    print(sevens_in_a_row([7, 2, 1, 6, 2], 1))


if __name__ == '__main__':
    main()
