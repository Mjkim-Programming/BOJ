n, x = input().split()
n = int(n)
x = int(x)

a = list(input().split())
a = [int(i) for i in a]

print(*(filter(lambda b: b < x, a)))