def bishop_max(n, board):
    def dfs(pos, color, count):
        nonlocal max_count
        if pos >= len(cells):
            max_count = max(max_count, count)
            return
        
        y, x = cells[pos]
        if not d1[y + x] and not d2[y - x + n - 1]:
            d1[y + x] = d2[y - x + n - 1] = True
            dfs(pos + 1, color, count + 1)
            d1[y + x] = d2[y - x + n - 1] = False
        
        dfs(pos + 1, color, count)
    
    result = 0
    for color in [0, 1]:
        cells = [(y, x) for y in range(n) for x in range(n) if board[y][x] == 1 and (y + x) % 2 == color]
        d1 = [False] * (2 * n)
        d2 = [False] * (2 * n)
        max_count = 0
        dfs(0, color, 0)
        result += max_count
    return result

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
print(bishop_max(n, board))
