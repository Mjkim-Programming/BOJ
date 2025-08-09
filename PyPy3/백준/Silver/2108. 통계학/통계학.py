from collections import Counter

n = int(input())
arr = []

for _ in range(0, n):
    arr.append(int(input()))

count = Counter(arr)
max_freq = max(count.values())

nums = [num for num, freq in count.items() if freq == max_freq]
nums.sort()
arr_sorted = arr
arr_sorted.sort()

print(int(round(sum(arr)/n, 0)))
print(arr_sorted[len(arr_sorted)//2])
if len(nums) == 1:
    print(*nums)
else:
    print(nums[1])
print(max(arr) - min(arr))
