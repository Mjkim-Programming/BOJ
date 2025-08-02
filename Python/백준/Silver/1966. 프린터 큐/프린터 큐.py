test_case_num = int(input())

for i in range(0, test_case_num):
    n, m = input().split()
    n = int(n)
    m = int(m)
    priority_list = list(input().split())
    index_list = list(range(n))
    count = 0
    
    while True:
        if priority_list[0] < max(priority_list):
            priority_list.append(priority_list.pop(0))
            index_list.append(index_list.pop(0))
        else:
            count += 1
            if index_list[0] == m:
                print(count)
                break
            priority_list.pop(0)
            index_list.pop(0)