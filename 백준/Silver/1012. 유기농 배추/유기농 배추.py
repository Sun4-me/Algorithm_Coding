import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

dx = [1, 0, -1, 0]  # 우 하 좌 상
dy = [0, 1, 0, -1]


def dfs(y, x):
    visited[y][x] = 1

    for direct in range(4):
        ny, nx = y + dy[direct], x + dx[direct]
        if (0 <= ny <= n - 1) and (0 <= nx <= m - 1):
            if visited[ny][nx] == 0 and grid[ny][nx] == 1:
                dfs(ny, nx)


t = int(input())
for case in range(t):
    m, n, k = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(k)]
    grid = [[0] * m for _ in range(n)]  # 배추 위치
    visited = [[0] * m for _ in range(n)]  # 배추 방문 여부

    # 배추 위치 저장
    for row in nodes:
        grid[row[1]][row[0]] = 1

    cnt = 0  # 지렁이 수
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 1 and visited[row][col] != 1:
                dfs(row, col)
                cnt += 1

    print(cnt)
