N,K=map(int, input().split())
A=[]
for i in range(1,N+1):
    if N%i==0:
        A.append(i)
for i in range(N):
    A.append(0)
if (A[K-1])!=0:
    print(A[K-1])
else:
    print('0')