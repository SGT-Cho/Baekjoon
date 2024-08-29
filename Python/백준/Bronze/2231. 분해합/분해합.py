N=int(input())
if N==1:
    print(0)
else:
    for i in range(1,N):
        s=''
        s+=str(i)
        sum=0
        check=0
        for j in range(len(s)):
            sum+=int(s[j])
        if i + sum ==N:
            print(i)
            check+=1
            break
    if check==0:
        print(0)
