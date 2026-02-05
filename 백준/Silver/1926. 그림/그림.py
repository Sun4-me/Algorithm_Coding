from collections import deque


def bfs(y, x):
    v[y][x] = 1
    q = deque([(y, x)])
    area = 1

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx] == 1 and v[ny][nx] == 0:
                    v[ny][nx] = 1
                    area += 1
                    q.append((ny, nx))

    return area


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]

cnt = 0
res = 0
for row in range(n):
    for col in range(m):
        if v[row][col] == 0 and grid[row][col] == 1:
            cnt += 1
            res = max(res, bfs(row, col))

print(cnt)
print(res)
