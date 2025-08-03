n = int(input())
q = []

for _ in range(0, n):
    order = input()
    if(order == "top"):
        try:
            print(q[-1])
        except:
            print(-1)
    elif(order == "empty"):
        if(len(q) == 0):
            print(1)
        else:
            print(0)
    elif(order == "size"):
        print(len(q))
    elif(order == "pop"):
        try:
            print(q.pop(0))
        except IndexError:
            print(-1)
    elif(order == "front"):
        try:
            print(q[0])
        except:
            print(-1)
    elif(order == "back"):
        try:
            print(q[-1])
        except:
            print(-1)
    else:
        _, num = order.split()
        q.append(num)