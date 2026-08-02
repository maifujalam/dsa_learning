def is_leap_year(x):
    if x%4==0 and x%100 !=0:
        return True
    if x%100 ==0 and x%400 ==0:
        return True
    return False

if __name__ == "__main__":
    print(is_leap_year(1900))
    print(is_leap_year(2000))
    print(is_leap_year(2001))