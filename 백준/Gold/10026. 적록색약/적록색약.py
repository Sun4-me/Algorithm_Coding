import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [1, 0, -1, 0]  # 우 하 좌 상
dy = [0, 1, 0, -1]


def dfs(y, x):
    visited[y][x] = 1

    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx <= n - 1 and 0 <= ny <= n - 1:
            if visited[ny][nx] == 0 and grid[ny][nx] == color:
                dfs(ny, nx)


n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

cnt_1 = 0
for row in range(n):
    for col in range(n):
        for i in ("R", "G", "B"):
            color = i

            if visited[row][col] == 0 and grid[row][col] == color:
                dfs(row, col)
                cnt_1 += 1

# 적록색약용
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == "G":
            grid[i][j] = "R"

cnt_2 = 0
for row in range(n):
    for col in range(n):
        for i in ("R", "B"):
            color = i
            if visited[row][col] == 0 and grid[row][col] == color:
                dfs(row, col)
                cnt_2 += 1
                
print(cnt_1, cnt_2)
