import sys

input = sys.stdin.readline

N, M, B = map(int, input().strip().split())
land = [list(map(int, input().strip().split())) for _ in range(N)]

min_time = 10**9
result_height = 0

for target_height in range(257):
    remove_blocks = 0
    add_blocks = 0

    for i in range(N):
        for j in range(M):
            diff = land[i][j] - target_height
            if diff > 0:
                remove_blocks += diff
            else:
                add_blocks -= diff

    if remove_blocks + B >= add_blocks:
        time = remove_blocks * 2 + add_blocks
        if time <= min_time:
            min_time = time
            result_height = target_height

print(min_time, result_height)