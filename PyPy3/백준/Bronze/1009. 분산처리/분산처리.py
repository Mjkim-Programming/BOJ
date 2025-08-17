N = int(input())

def last_digit(a, b):
    res = pow(a, b, 10)
    return 10 if res == 0 else res

for _ in range(N):
    a, b = map(int, input().split())
    print(last_digit(a, b))