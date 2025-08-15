import itertools

A, B, C, D = map(int, input().split())
nums = [A, B, C, D]

max_area = 0
for p in itertools.permutations(nums):
    w = min(p[0], p[2])
    h = min(p[1], p[3])
    max_area = max(max_area, w * h)

print(max_area)
