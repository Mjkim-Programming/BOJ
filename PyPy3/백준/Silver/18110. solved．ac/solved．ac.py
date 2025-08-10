n = int(input())

def custom_round(x):
    return int(x + 0.5)

if n == 0:
    print(0)
else:
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    cut = custom_round(n * 0.15)
    result = arr[cut:n-cut]

    avg = sum(result) / len(result)
    print(custom_round(avg))