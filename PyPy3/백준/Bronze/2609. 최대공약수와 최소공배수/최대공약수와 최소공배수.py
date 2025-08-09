a, b = map(int, input().split())
a_eu = a
b_eu = b
while b_eu != 0:
    a_eu, b_eu = b_eu, a_eu%b_eu
    
print(a_eu)
print(a*b//a_eu)