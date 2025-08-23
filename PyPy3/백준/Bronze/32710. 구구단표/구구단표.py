s = set()
for A in range(2, 10):
    for B in range(1, 10):
        s.update([A, B, A*B])
print(1 if int(input()) in s else 0)
