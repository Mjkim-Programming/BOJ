n = int(input())
stack = []

for _ in range(0, n):
    order = input()
    if(order == "top"):
        try:
            print(stack[-1])
        except:
            print(-1)
    elif(order == "empty"):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    elif(order == "size"):
        print(len(stack))
    elif(order == "pop"):
        try:
            print(stack.pop())
        except IndexError:
            print(-1)
    else:
        _, num = order.split()
        stack.append(num)