n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

def repaint_count(x, y):
    cnt_w = 0
    cnt_b = 0
    for i in range(8):
        for j in range(8):
            current = board[x+i][y+j]
            if (i + j) % 2 == 0:
                if current != 'W':
                    cnt_w += 1
                if current != 'B':
                    cnt_b += 1
            else:
                if current != 'B':
                    cnt_w += 1
                if current != 'W':
                    cnt_b += 1
    return min(cnt_w, cnt_b)

min_count = 64
for i in range(n - 7):
    for j in range(m - 7):
        min_count = min(min_count, repaint_count(i, j))

print(min_count)