import sys

sys.setrecursionlimit(10 ** 6)


def dfs(y, x):
    global area
    v[y][x] = 1

    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m:
            if grid[ny][nx] == 1 and v[ny][nx] == 0:
                area += 1
                dfs(ny, nx)


n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]

cnt = 0
res = 0
for row in range(n):
    for col in range(m):
        if v[row][col] == 0 and grid[row][col] == 1:
            cnt += 1
            area = 1
            dfs(row, col)
            res = max(res, area)

print(cnt)
print(res)
