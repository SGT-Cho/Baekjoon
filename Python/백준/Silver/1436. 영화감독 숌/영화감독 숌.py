N=int(input())
a=[]
for i in range(10000000):
    if '666' in str(i):
        a.append(i)
print(a[N-1])