from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
count_arr = Counter(arr)

m = int(input())
arr2 = list(map(int, input().split()))
arr3 = []
for i in arr2:
    arr3.append(count_arr[i])
    
print(*arr3)