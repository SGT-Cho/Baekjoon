N,M=map(int, input().split())
S=input().split()
S=list(map(int,S))
new=[]
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            new.append(S[i]+S[j]+S[k])
new=list(set(new))
new.append(M)
new = [item for item in new if item <= M]
new.sort()
print(new[-2])