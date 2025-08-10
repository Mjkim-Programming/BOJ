import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * k
    id = 0

    for _ in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            heapq.heappush(min_heap, (num, id))
            heapq.heappush(max_heap, (-num, id))
            visited[id] = True
            id += 1
        else:
            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])