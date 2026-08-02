mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
t=13

def bina(arr,tr):
    l=0
    r=len(arr)-1
    while l<=r:
        mid = (l+r)// 2
        if arr[mid]==tr:
            print("Found at index", mid)
            return mid
        if arr[mid]<tr:
            l=mid+1
        else:
            r=mid-1
    return -1
if __name__ == "__main__":
    print(bina(mylist,t))
