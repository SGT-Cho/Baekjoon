N=int(input())
X=[]
Y=[]
for i in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
print((X[-1]-X[0])*(Y[-1]-Y[0]))