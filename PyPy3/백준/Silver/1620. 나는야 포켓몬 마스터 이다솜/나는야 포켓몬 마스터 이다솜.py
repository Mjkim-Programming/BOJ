from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())

dq = deque()
name_to_index = {}

for i in range(N):
    name = sys.stdin.readline().strip()
    dq.append(name)
    name_to_index[name] = i + 1

for _ in range(M):
    query = sys.stdin.readline().strip()
    if query.isdigit():
        print(dq[int(query) - 1])
    else:
        print(name_to_index[query])