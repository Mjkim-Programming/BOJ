n = int(input())
seq = list(map(int, input().split()))

if n == 1:
    print("A")
elif n == 2:
    if seq[0] == seq[1]:
        print(seq[0])
    else:
        print("A")
else:
    x0, x1, x2 = seq[0], seq[1], seq[2]
    if x1 == x0:
        if x2 != x1:
            print("B")
            exit()
        else:
            a, b = 1, 0
    else:
        if (x2 - x1) % (x1 - x0) != 0:
            print("B")
            exit()
        a = (x2 - x1) // (x1 - x0)
        b = x1 - x0 * a

    valid = True
    for i in range(n - 1):
        if seq[i] * a + b != seq[i + 1]:
            valid = False
            break

    if not valid:
        print("B")
    else:
        print(seq[-1] * a + b)