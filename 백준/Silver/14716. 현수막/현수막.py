from collections import deque

# 상 하 좌 우 상좌 상우 하좌 하우
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]


def bfs(y, x):
    q = deque([(y, x)])
    visited[y][x] = 1

    while q:
        cy, cx = q.popleft()

        for k in range(8):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < m and 0 <= nx < n:
                if visited[ny][nx] == 0 and grid[ny][nx] == 1:
                    visited[ny][nx] = 1
                    q.append((ny, nx))


###################################
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
###################################
visited = [[0] * n for _ in range(m)]
res = 0
for row in range(m):
    for col in range(n):
        if grid[row][col] == 1 and visited[row][col] == 0:
            bfs(row, col)
            res += 1

print(res)
