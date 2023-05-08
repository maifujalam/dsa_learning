import itertools
def find_max_elements(array):
    # Write your code here
    l=len(array)
    target=array[0]
    ans=0
    print(target)
    for i in range(l,0,-1):
        com=itertools.combinations(array[1:],i)
        for j in com:
            if target == sum(j):
                ans=len(j)
                break
        if ans!=0:
            break
    print(ans)


if __name__ == '__main__':
    #find_max_elements([10, 2, 3, 5, 5])
    find_max_elements([4, 5, 3, 3, 3])

