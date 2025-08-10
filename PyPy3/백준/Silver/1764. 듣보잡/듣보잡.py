import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

a = []
b = []

for _ in range(n):
    a.append(input().strip())
for _ in range(m):
    b.append(input().strip())

a_set = set(a)
b_set = set(b)

inter = a_set & b_set
sorted = list(inter)
sorted.sort()
print(len(inter))
for i in sorted:
    print(i)