N=int(input())
cnt=0

for i in range(N):
    a=[]
    cnt2=1
    S=input()
    for j in range(len(S)):
        if S[j] not in a:
            a.append(S[j])
        elif S[j] in a and S[j]!=S[j-1]:
            cnt2=cnt2*0
    cnt+=cnt2
print(cnt)