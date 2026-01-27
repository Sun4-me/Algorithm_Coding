import sys

input = sys.stdin.readline
sys.setrecursionlimit(30000)

dx = [1, 0, -1, 0, -1, 1, -1, 1]  # 우 하 좌 상 대상좌 대상우 대하좌 대하우
dy = [0, 1, 0, -1, -1, -1, 1, 1]


def dfs(y, x):
    global cnt
    visited[y][x] = 1
    cnt += 1

    for direction in range(8):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx <= w - 1 and 0 <= ny <= h - 1:
            if visited[ny][nx] == 0 and grid[ny][nx] == 1:
                dfs(ny, nx)


while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    land = []
    for row in range(h):
        for col in range(w):
            if visited[row][col] == 0 and grid[row][col] == 1:
                cnt = 0
                dfs(row, col)
                land.append(cnt)

    print(len(land))
