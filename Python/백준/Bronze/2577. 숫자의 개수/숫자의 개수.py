a = int(input())
b = int(input())
c = int(input())

res = list(str(a * b * c))
res = [int(i) for i in res]
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in res:
    count[i] += 1

for i in count:
    print(i)