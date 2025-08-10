import math

n = int(input())
num_str_list = list(str(math.factorial(n))[::-1])
c = 0

for s in num_str_list:
    if s == '0':
        c += 1
    else:
        break
        
print(c)