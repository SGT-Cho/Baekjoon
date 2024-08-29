N, M = map(int, input().split())
T = []
for _ in range(N):
    T.append(input())

W = [['W' if (i + j) % 2 == 0 else 'B' for j in range(8)] for i in range(8)]
B = [['B' if (i + j) % 2 == 0 else 'W' for j in range(8)] for i in range(8)]

min_count = float('inf')

for y in range(N - 7):
    for x in range(M - 7):
        countW = 0
        countB = 0
        for i in range(8):
            for j in range(8):
                if T[y + i][x + j] != W[i][j]:
                    countW += 1
                if T[y + i][x + j] != B[i][j]:
                    countB += 1
        min_count = min(min_count, countW, countB)

print(min_count)
