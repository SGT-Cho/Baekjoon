N=int(input())
s=input().split()
total=0
for i in range(N):
    if int(s[i])>1:
        count=1
        for j in range(2,int(s[i])):
            if int(s[i])%j==0:
                count*=0
        total+=count
print(total)
