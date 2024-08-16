def print_pattern(N):
    for i in range(N):
        print(' ' * (N - i - 1) + '*' * (2 * i + 1))
    
    # Lower part of the pattern
    for i in range(N - 2, -1, -1):
        print(' ' * (N - i - 1) + '*' * (2 * i + 1))

# Example usage:
N = int(input())
print_pattern(N)