import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left, right = 0, N - 1
closest_sum = float('inf')
res = (0, 0)

while left < right:
    s = arr[left] + arr[right]
    
    if abs(s) < abs(closest_sum):
        closest_sum = s
        res = (arr[left], arr[right])
    
    if s < 0:
        left += 1
    elif s > 0:
        right -= 1
    else:
        break

print(res[0], res[1])
