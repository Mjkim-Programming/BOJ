stack = []
prior = {
    '+': 1,
    '-': 1,
    '(': -1,
    ')': -2,
    '*': 2,
    '/': 2
}
res = ""

exp = input()
for ch in exp:
    if ch.isalpha():
        res += ch
    elif prior[ch] == -1:
        stack.append(ch)
    elif prior[ch] == -2:
        while stack and stack[-1] != "(":
            res += stack.pop()
        stack.pop()
    else:
        while stack and stack[-1] != '(' and prior[stack[-1]] >= prior[ch]:
            res += stack.pop()
        stack.append(ch)

while stack:
    res += stack.pop()
    
print(res)