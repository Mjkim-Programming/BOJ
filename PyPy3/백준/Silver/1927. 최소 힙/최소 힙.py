import sys
import heapq

input = sys.stdin.readline

arr = []

n = int(input())
for _ in range(n):
    query = int(input())
    if query == 0:
        try:
            print(heapq.heappop(arr))
        except:
            print(0)
    else:
        heapq.heappush(arr, query)