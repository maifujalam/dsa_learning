from cmath import inf

ar=[1,3,6,7,9]
ar2=[1,3,2,6,5]
def checker(arr):
    small=large=arr[0]
    for i in arr:
        small=min(small,i)
        large=max(large,i)
    sSmall=large
    sLarge=small
    for i in arr:
        if i<sSmall and i!=small:
            sSmall=i
        if i>sLarge and i!=large:
            sLarge=i
    return small,large,sSmall,sLarge


if __name__ =="__main__":
    print(checker(ar))
    print(checker(ar2))
