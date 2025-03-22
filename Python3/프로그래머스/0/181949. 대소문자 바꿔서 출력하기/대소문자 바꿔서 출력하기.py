str = input()

for i in str:
    if i.isupper() == True:
        print(i.lower(), end = "")
    elif i.islower() == True:
        print(i.upper(), end = "")