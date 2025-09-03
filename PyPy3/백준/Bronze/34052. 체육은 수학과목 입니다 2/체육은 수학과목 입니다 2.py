arr = []
for _ in range(4):
    arr.append(int(input()))
arr.append(300)
if sum(arr) > 1800:
    print("No")
else:
    print("Yes")