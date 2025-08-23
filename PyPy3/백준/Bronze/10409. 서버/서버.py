N, T = map(int, input().split())
arr = list(map(int, input().split()))

res = 0
cnt = 0
for t in arr:
    res += t
    if res <= T:
        cnt += 1
    else:
        break
print(cnt)