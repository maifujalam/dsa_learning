import itertools


def find_max_elements(a,array):
    # Write your code here
    l = len(array)
    target = array[0]
    ans = 0
    #print(target)
    for i in range(l, 0, -1):
        com = itertools.combinations(array, i)
        for j in com:
            #print(j)
            if max(j)-min(j)==a:
                #print(j)
                #print(len(j))
                ans=len(j)
        if ans!=0:
            break
    print(ans)


if __name__ == '__main__':
    # find_max_elements([10, 2, 3, 5, 5])
    find_max_elements(2, [8, 4, 2, 6, 100, 101, 101, 110, 102])
