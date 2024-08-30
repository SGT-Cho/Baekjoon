s=input()
a=[]
for i in range(len(s)):
    a.append(s[i])

a=list(map(int,a))
a.sort()
a.reverse()
a=list(map(str,a))
print(''.join(a))
