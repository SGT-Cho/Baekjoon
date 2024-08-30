#10814
N=int(input())
D=[[''for col in range(3)]for row in range(N)]
for i in range(N):
    age, name=map(str, input().split())
    D[i][0]=int(age) #str int 구분할것!!!!!!!!!!!!!!!!!!!!!!!!!
    D[i][1]=i
    D[i][2]=name
D.sort()
for i in range(N):
    print(D[i][0],D[i][2])

