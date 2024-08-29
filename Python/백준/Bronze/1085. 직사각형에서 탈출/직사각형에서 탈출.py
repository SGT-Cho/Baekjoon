x,y,w,h=map(int, input().split())
A=[x,y,w-x,h-y]
A.sort()
print(A[0])