while True:
    n=int(input())
    if n==-1:
        break
    else:
        X=[]
        s=''
        total=0
        for i in range(1,n+1):
            if n%i==0 and n!=i:
                X.append(i)
                total+=i
        if total==n:
            s+=str(n)
            s+=' = '
            s+=' + '.join(map(str,X))
        else:
            s+=str(n)
            s+=' is NOT perfect.'

    print(s)
