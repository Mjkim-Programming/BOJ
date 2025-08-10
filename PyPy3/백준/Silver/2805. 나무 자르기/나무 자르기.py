n, m = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for tree in arr:
        if tree > mid:
            total += tree - mid

    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)