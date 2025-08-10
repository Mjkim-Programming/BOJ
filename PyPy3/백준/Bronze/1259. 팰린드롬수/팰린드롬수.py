while True:
    n = int(input())
    num_str = str(n)
    if n == 0: break
    if num_str == num_str[::-1]:
        print("yes")
    else:
        print("no")