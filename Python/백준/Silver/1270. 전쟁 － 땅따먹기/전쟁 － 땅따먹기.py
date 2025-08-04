from collections import Counter

n = int(input())

total_list = []

for _ in range(n):
    temp = list(input().split())
    temp = [int(i) for i in temp]
    total_list.append(temp)

for i in range(n):
    total = total_list[i][0]
    people = total_list[i][1:]
    
    counter = Counter(people)
    
    out = "SYJKGW"
    for j in counter:
        if counter[j] > (total / 2):
            out = j
            break
    print(out)
            