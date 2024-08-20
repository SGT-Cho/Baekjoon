s=''
l = [[-1 for col in range(15)] for row in range(5)]
for i in range(5):
    letters=input()
    for j in range(len(letters)):
        l[i][j]=letters[j]
k=0
while k<15:
    for x in range(15):
        for y in range(5):
            if l[y][x]!= -1:
                s+=str(l[y][x])
        k+=1
print(s)