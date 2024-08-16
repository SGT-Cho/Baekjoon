S=input()
a=[]*26
b=[]
cnt=[0]*26
qm=0
for i in range(len(S)):
    b.append(ord(S[i])-65) #0~25 대문자 32~57소문자
    if b[i]> 26:
        b[i]-=32
for j in range(len(b)):
    cnt[b[j]]+=1
largest=0
for k in range(26):
    if largest<cnt[k]:
        largest=cnt[k]
for l in range(26):
    if largest==cnt[l]:
        qm+=1
if qm>1:
    print("?")
else:
    print(chr(cnt.index(largest)+65))