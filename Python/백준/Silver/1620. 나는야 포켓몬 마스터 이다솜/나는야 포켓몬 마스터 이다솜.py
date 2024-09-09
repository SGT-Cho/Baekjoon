N,M=map(int,input().split())
dogam={}
for i in range(N):
    dogam[input()]=str(i+1)
magod={v:k for k,v in dogam.items()}
for i in range(M):
    a=input()
    try:
        print(dogam[a])
    except:
        print(magod[a])