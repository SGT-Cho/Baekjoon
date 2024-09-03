N,M=map(int,input().split())
S=[]
A=[]
count=0
for i in range(N):
    S.append(input())
for j in range(M):
    word=input()
    A.append(word)
new=[]
for items in S:
    if items not in new:
        new.append(items)
for items2 in A:
    if items2 in new:
        count+=1
print(count)