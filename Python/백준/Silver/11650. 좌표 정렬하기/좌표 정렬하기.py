import sys

# 입력 받기
N = int(sys.stdin.readline())
points = []

# 점 입력 받기
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

# 정렬
points.sort()

# 출력
for point in points:
    print(point[0], point[1])
