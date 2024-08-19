M=9
N=9
A = [[0 for col in range(N)] for row in range(M)]
largest=-1
idx=[0,0]
for row in range(M):
    x=input().split()
    for col in range(N):
        A[row][col]=x[col]
        if int(x[col])> int(largest):
            largest=x[col]
            idx[0]=row+1
            idx[1]=col+1
print(largest)
print(idx[0],idx[1])
