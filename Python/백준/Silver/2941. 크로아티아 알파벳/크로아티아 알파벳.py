S=input()
S=S+' '+' '
cnt=0
i=0
while i <len(S)-2:
    if S[i]=='c' and S[i+1]=='=':
        cnt+=1
        i+=2
    elif S[i]=='c' and S[i+1]=='-':
        cnt+=1
        i+=2
    elif S[i]=='d' and S[i+1]=='z' and S[i+2]=='=':
        cnt+=1
        i+=3
    elif S[i]=='d' and S[i+1]=='-':
        cnt+=1
        i+=2
    elif S[i]=='l' and S[i+1]=='j':
        cnt+=1
        i+=2
    elif S[i]=='n' and S[i+1]=='j':
        cnt+=1
        i+=2
    elif S[i]=='s' and S[i+1]=='=':
        cnt+=1
        i+=2
    elif S[i]=='z' and S[i+1]=='=':
        cnt+=1
        i+=2
    else:
        cnt+=1
        i+=1

print(cnt)
    
    