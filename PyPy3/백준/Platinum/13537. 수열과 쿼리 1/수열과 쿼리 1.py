import sys
import bisect
input = sys.stdin.readline

def build(node, start, end):
    if start == end:
        tree[node] = [arr[start]]
    else:
        mid = (start + end) // 2
        build(node*2, start, mid)
        build(node*2+1, mid+1, end)
        tree[node] = sorted(tree[node*2] + tree[node*2+1])

def query(node, start, end, l, r, k):
    if r < start or end < l:
        return 0
    if l <= start and end <= r:
        return len(tree[node]) - bisect.bisect_right(tree[node], k)
    mid = (start + end) // 2
    return query(node*2, start, mid, l, r, k) + query(node*2+1, mid+1, end, l, r, k)

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

tree = [[] for _ in range(4*N)]
build(1, 0, N-1)

for _ in range(M):
    i, j, k = map(int, input().split())
    print(query(1, 0, N-1, i-1, j-1, k))
