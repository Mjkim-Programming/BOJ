n = int(input())
arr = list(map(int, input().split()))
arr.sort()

res = 0
total = 0

for time in arr:
    total += time
    res += total

print(res)