n = int(input())
arr = list(map(int, input().split()))

lis = [1] * n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            lis[i] = max(lis[i], lis[j] + 1)

lds = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[j] < arr[i]:
            lds[i] = max(lds[i], lds[j] + 1)

max_len = 0
for i in range(n):
    max_len = max(max_len, lis[i] + lds[i] - 1)

print(max_len)