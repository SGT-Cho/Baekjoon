A,B=111111,111111
while A!=0 and B!=0:
    A,B=map(int, input().split())
    if A==0 and B==0:
        break
    if A%B==0:
        print('multiple')
    elif B%A==0:
        print('factor')
    else:
        print('neither')