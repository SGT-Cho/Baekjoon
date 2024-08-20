T=int(input())
for i in range(T):
    c=[0,0,0,0]
    money=int(input())
    while money >=25:
        c[0]+=1
        money-=25
    while money >=10:
        c[1]+=1
        money-=10
    while money >=5:
        c[2]+=1
        money-=5
    while money >=1:
        c[3]+=1
        money-=1
    print(c[0],c[1],c[2],c[3])