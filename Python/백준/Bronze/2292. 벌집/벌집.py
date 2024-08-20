N=int(input())
A=[1]
if N==1:
    print(1)
    #exit(0)
for i in range(1,20000):
    A.append(A[i-1]+6*(i))
    if N>A[i-1] and N<=A[i]:
        print(i+1)