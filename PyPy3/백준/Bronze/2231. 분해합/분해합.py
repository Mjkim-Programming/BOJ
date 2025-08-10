import sys

N = int(sys.stdin.readline().strip())
digits = len(str(N))
start = max(1, N - 9 * digits)

def decomposed(x):
    s = x
    while x:
        s += x % 10
        x //= 10
    return s

ans = 0
for i in range(start, N):
    if decomposed(i) == N:
        ans = i
        break

print(ans)