s=0
N, B =map(str, input().split())
B=int(B)
for i in range(1,len(N)+1):
    if ord(N[-i])>=48 and ord(N[-i]) <=57:
        s+=int(N[-i])*(pow(B,i-1))
    else:
        s+=(ord(N[-i])-55)*(pow(B,i-1))
print(s)