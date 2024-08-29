a1,a0=map(int,input().split())
c=int(input())
n0=int(input())
label=1
for i in range(n0,n0+10000):
    if ((c*i)-(a1*i)-a0)<0:
        label*=0
print(label)

