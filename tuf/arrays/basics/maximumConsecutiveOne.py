a1=[1,1,0,0,1,0]

ans = 0
n = 0
for i in range(len(a1)):
    if a1[i]==1:
        n+=1
    else:
        ans=max(ans,n)
        n=0
print(ans)