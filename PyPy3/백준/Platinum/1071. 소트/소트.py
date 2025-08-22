from collections import Counter

def num_insert(index):
    global a_len
    while count[index]:
        ans.append(index)
        count[index] -= 1
        a_len -= 1

n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
a_len = n
sort_num = sorted(count)
ans = list()
while a_len > 0:
    for k in range(len(sort_num)):
        flag = True
        i = sort_num[k]
        if count[i] != 0:
            if i + 1 in sort_num and count[i + 1] != 0:
                for j in sort_num[k + 1:]:
                    if i + 2 <= j and count[j] != 0:
                        num_insert(i)
                        ans.append(j)
                        count[j] -= 1
                        a_len -= 1
                        flag = False
                        break
                if flag:
                    ans.append(i + 1)
                    count[i + 1] -= 1
                    a_len -= 1
            else:
                num_insert(i)
print(*ans)