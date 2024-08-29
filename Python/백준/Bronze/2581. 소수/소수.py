def isPrime(a):
    check=1
    if a <2:
        check=0
    for i in range(2,a):
        if a%i==0:
            check*=0
    if check:
        return a



M=int(input())
N=int(input())
X=[]
for i in range(M,N+1):
    if isPrime(i):
        X.append(isPrime(i))

if len(X)>0:
    print(sum(X))
    print(X[0])
else:
    print(-1)