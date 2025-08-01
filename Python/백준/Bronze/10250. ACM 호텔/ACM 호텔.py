num = int(input())

for _ in range(0, num):
    floor, room, number = input().split()
    floor = int(floor)
    room = int(room)
    number = int(number)
    
    if number % floor == 0:
        fl = floor
        rn = number // floor
    else:
        fl = number % floor
        rn = number // floor + 1
    
    print(str(fl)+str(rn).zfill(2))