a=[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]

# zeroCount=0
# ans=[]
# for i in a:
#     if i==0:
#         zeroCount+=1
#     else:
#         ans.append(i)
# for i in range(zeroCount):
#     ans.append(0)
# print(ans)
i=0
j=i+1

for i in range(0,len(a)):
    if a[i]==0:
        for j in range(i+1,len(a)):
            if a[j]!=0:
                a[i],a[j]=a[j],a[i]
            i=j
print(a)