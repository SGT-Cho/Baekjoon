A=[]
B=[]
N=int(input())
a=list(map(int, input().split()))
for i in range(N):
    A.append(a[i])
M=int(input())
b=list(map(int, input().split()))
for j in range(M):
    B.append(b[j])

A=set(A)
for k in range(len(B)):
    if B[k] in A:
        B[k]=1
    else:
        B[k]=0
B=list(map(str,B))
print(" ".join(B))