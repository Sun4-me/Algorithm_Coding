import sys
from pprint import *

sys.setrecursionlimit(10000)

input = sys.stdin.readline

dx = [1, 0, -1, 0]  # 우 하 좌 상
dy = [0, 1, 0, -1]


def dfs(y, x):
    global square
    visited[y][x] = 1
    square += 1

    for direct in range(4):
        nx = x + dx[direct]
        ny = y + dy[direct]
        if (0 <= ny <= m - 1) and (0 <= nx <= n - 1):
            if visited[ny][nx] == 0 and grid[ny][nx] == 0:
                dfs(ny, nx)


# 가로, 세로, k개 직사각형
m, n, k = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(k)]
grid = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]

# 직사각형 그리기
for row in nodes:
    for y in range(row[1], row[3]):
        for x in range(row[0], row[2]):
            grid[y][x] += 1

# 분리된 각 영역의 넓이 구하기
square_lst = []
for row in range(m):
    for col in range(n):
        if grid[row][col] == 0 and visited[row][col] == 0:
            square = 0
            dfs(row, col)
            square_lst.append(square)

square_lst.sort()
print(len(square_lst))
print(*square_lst)
