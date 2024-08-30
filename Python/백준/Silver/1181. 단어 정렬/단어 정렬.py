#1181
N=int(input())
D=[[''for col in range(2)]for row in range(N)]
S=[]
for i in range(N):
    s=input()
    D[i][1]=s
    D[i][0]=len(s)
D.sort()
for i in range(N):
    S.append((D[i][1]))
temp=[]
for items in S:
    if items not in temp:
        temp.append(items)
for i in range(len(temp)):
    print(temp[i])