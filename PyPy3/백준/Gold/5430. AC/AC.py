from collections import deque

n = int(input())
for _ in range(n):
    query = list(input().strip())
    num = int(input())
    arr_str = input().strip()
    if num == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr_str[1:-1].replace(" ", "").split(",")))
    is_reversed = False
    try:
        for q in query:
            if q == "R":
                is_reversed = not is_reversed
            else:
                if is_reversed:
                    arr.pop()
                else:
                    arr.popleft()
        if is_reversed:
            print("[" + ",".join(map(str, reversed(arr))) + "]")
        else:
            print("[" + ",".join(map(str, arr)) + "]")
    except:
        print("error")