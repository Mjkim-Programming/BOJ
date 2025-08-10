K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    cnt = sum(l // mid for l in lan)

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)