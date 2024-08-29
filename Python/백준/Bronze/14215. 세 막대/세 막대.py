A,B,C=map(int, input().split())
K=[A,B,C]
K.sort()
while True:
    if K[2]>=K[1]+K[0]:
        K[2]-=1
        K.sort
    if K[2]<K[1]+K[0]:
        print(sum(K))
        break