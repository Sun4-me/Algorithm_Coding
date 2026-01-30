from collections import deque


########################################################

def bfs(y, x):
    q = deque([(y, x)])
    grid[y][x] = 1

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            ny, nx = cy + dy, cx + dx
            if ny < 0:
                ny = n - 1
            elif ny >= n:
                ny = 0
            elif nx < 0:
                nx = m - 1
            elif nx >= m:
                nx = 0
            if grid[ny][nx] == 0:
                grid[ny][nx] = 1
                q.append((ny, nx))


########################################################
# 세로 가로 | 최대 100
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
########################################################


cnt = 0
for row in range(n):
    for col in range(m):
        if grid[row][col] == 0:
            bfs(row, col)
            cnt += 1

print(cnt)
