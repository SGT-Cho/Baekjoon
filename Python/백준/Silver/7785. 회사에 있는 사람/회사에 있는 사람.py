N = int(input())
current = set()
for i in range(N):
    name, status = input().split()
    
    if status == 'enter':
        current.add(name)
    else:
        current.discard(name)

for name in sorted(current, reverse=True):
    print(name)