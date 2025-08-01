asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = [8, 7, 6, 5, 4, 3, 2, 1]

a = list(input().split())
a = [int(i) for i in a]

if a == asc:
    print("ascending")
elif a == des:
    print("descending")
else:
    print("mixed")