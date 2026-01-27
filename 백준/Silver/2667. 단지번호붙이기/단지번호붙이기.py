import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [1, 0, -1, 0]  # 우 하 좌 상
dy = [0, 1, 0, -1]


def dfs(y, x):
    global cnt
    visited[y][x] = 1
    cnt += 1

    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx <= n - 1 and 0 <= ny <= n - 1:
            if visited[ny][nx] == 0 and grid[ny][nx] == 1:
                dfs(ny, nx)


n = int(input())
grid = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

houses = []
for row in range(n):
    for col in range(n):
        if visited[row][col] == 0 and grid[row][col] == 1:
            cnt = 0
            dfs(row, col)
            houses.append(cnt)

houses.sort()
print(len(houses))
for i in houses:
    print(i)
