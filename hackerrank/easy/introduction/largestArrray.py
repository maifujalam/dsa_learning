def large(a):
    maxVal=a[0]
    for i in range(1,len(a)):
        if a[i]>maxVal:
            maxVal=a[i]
    return maxVal


if __name__ == "__main__":
    arr = [8, 10, 5, 7, 9]
    print(large(arr))
