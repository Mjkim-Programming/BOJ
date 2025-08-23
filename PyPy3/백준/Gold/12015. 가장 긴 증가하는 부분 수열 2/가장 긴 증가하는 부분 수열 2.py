import bisect

N = int(input())
A = list(map(int, input().split()))

lis = []
for x in A:
    if not lis or lis[-1] < x:
        lis.append(x)
    else:
        idx = bisect.bisect_left(lis, x)
        lis[idx] = x

print(len(lis))
