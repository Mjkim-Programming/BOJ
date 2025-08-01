import string

s = input()
alphabet = list(string.ascii_lowercase)

print(*(s.find(a) for a in alphabet))