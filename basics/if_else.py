if __name__ == '__main__':
    n = int(input().strip())
    print("Weird") if (n % 2 == 1 or (n % 2 == 0 and 6 <= n <= 20)) else print("Not Weird")


