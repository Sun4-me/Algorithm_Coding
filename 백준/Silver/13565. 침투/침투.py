from collections import deque


################################################

def bfs(y, x):
    q = deque([(y, x)])
    grid[y][x] = 1

    while q:
        cy, cx = q.popleft()

        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < m and 0 <= nx < n:
                if grid[ny][nx] == 0:
                    grid[ny][nx] = 1
                    q.append((ny, nx))


################################################
m, n = map(int, input().split())
grid = [list(map(int, input())) for _ in range(m)]
################################################
original = grid[-1].copy()

for col in range(n):
    if grid[0][col] == 0:
        bfs(0, col)

if original != grid[-1]:
    print("YES")
else:
    print("NO")
