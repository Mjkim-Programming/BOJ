a = input().split()
a = [int(i)**2 for i in a]
print(sum(a) % 10)