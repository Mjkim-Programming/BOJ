n = int(input())
files = [input().strip() for _ in range(n)]

pattern = ""
for chars in zip(*files):
    if all(c == chars[0] for c in chars):
        pattern += chars[0]
    else:
        pattern += "?"

print(pattern)