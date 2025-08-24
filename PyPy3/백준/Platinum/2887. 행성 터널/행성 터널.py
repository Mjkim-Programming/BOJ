import sys
input = sys.stdin.readline

N = int(input())

X = []
Y = []
Z = []

parent = [i for i in range(N)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def unite(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

points = []
for i in range(N):
    x, y, z = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))
    Z.append((z, i))

X.sort()
Y.sort()
Z.sort()

edges = []

for i in range(N-1):
    edges.append((X[i+1][0] - X[i][0], X[i][1], X[i+1][1]))
    edges.append((Y[i+1][0] - Y[i][0], Y[i][1], Y[i+1][1]))
    edges.append((Z[i+1][0] - Z[i][0], Z[i][1], Z[i+1][1]))

edges.sort()

total = 0
for val, a, b in edges:
    if find(a) != find(b):
        unite(a, b)
        total += val

print(total)
