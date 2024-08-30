import sys

# 입력 값 받기
N = int(sys.stdin.readline())
count = [0] * 10001  # 1부터 10000까지의 수를 카운트하기 위한 리스트

# 입력된 숫자들을 카운트 리스트에 반영
for _ in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

# 카운트 리스트를 기반으로 출력
for i in range(10001):
    if count[i] > 0:  # 해당 숫자가 등장한 적이 있는 경우에만 출력
        for _ in range(count[i]):
            sys.stdout.write(str(i) + '\n')
