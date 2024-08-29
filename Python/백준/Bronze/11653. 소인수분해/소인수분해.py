def isPrime(a):
    check=1
    if a <2:
        check=0
    for i in range(2,a):
        if a%i==0:
            check*=0
    if check:
        return a
    

def primeFactorization(n):
    X=[]
    while isPrime(n) ==  None:
        for i in range(2,int(n/2)+1):
            if isPrime(i):
                if n%i==0:
                    X.append(i)
                    n=int(n/i)
                    break
    if isPrime(n):
        X.append(n)
    return X
N=int(input())
if N>1:
    X=primeFactorization(N)
    for i in range(len(X)):
        print(X[i])