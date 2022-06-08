def leap(a):
    is_leap = False
    if a % 4 == 0 and a % 100 != 0:
        is_leap = True
    elif a % 100 == 0 and a % 400 == 0:
        is_leap = True

    return is_leap


if __name__ == '__main__':
    print(leap(2008))
