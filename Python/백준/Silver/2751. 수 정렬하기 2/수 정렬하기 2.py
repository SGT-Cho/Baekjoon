import sys
N = int(input())
a=[]
for i in range(N):
    a.append(int(sys.stdin.readline()))
a.sort()
for j in range(N):
    print(a[j])