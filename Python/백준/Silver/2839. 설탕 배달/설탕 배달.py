N=int(input())
res=[]
for i in range((N//3)+1):
    for j in range((N//5)+1):
        if 3*i+5*j==N:
            res.append(i+j)
if len(res)>0:
    res.sort()
    print(res[0])
else:
    print(-1)