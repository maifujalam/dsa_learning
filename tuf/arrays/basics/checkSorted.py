ar=[1,3,6,7,9]
ar2=[1,3,2,6,5]

def checker(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True


if __name__ == '__main__':
    print(checker(ar))
    print(checker(ar2))