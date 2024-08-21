X = int(input())
n = 1
while X > n:
    X -= n
    n += 1
if n % 2 == 0:
    numerator = X
    denominator = n - X + 1
else:
    numerator = n - X + 1
    denominator = X

print(f"{numerator}""/"f"{denominator}")
