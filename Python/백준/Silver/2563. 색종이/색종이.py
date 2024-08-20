s = [[0 for col in range(100)] for row in range(100)]
N=int(input())
for i in range(N):
    x,y=map(int, input().split())
    for a in range(10):
        for b in range(10):
            s[x+a][y+b]=1
print(sum(sum(s,[])))
