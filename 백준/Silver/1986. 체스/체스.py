from collections import deque
from pprint import *

# 세로 가로
n, m = map(int, input().split())
queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))

grid = [[0] * m for _ in range(n)]
############################################
pawns = []
for i in range(1, 2 * pawn[0], 2):
    r, c = pawn[i] - 1, pawn[i + 1] - 1
    pawns.append((r, c))
    grid[r][c] = 2  # 장애물

knights = []
for i in range(1, 2 * knight[0], 2):
    r, c = knight[i] - 1, knight[i + 1] - 1
    knights.append((r, c))
    grid[r][c] = 2

queens = []
for i in range(1, 2 * queen[0], 2):
    r, c = queen[i] - 1, queen[i + 1] - 1
    queens.append((r, c))
    grid[r][c] = 2

############################################
for i in queens:
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):  # 상 하 좌 우 상좌 상우 하좌 하우
        cy, cx = i[0], i[1]
        while True:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx] != 2: # 장애물아니면
                    grid[ny][nx] = 1 # 공격 가능한 위치
                    cy, cx = ny, nx
                else:
                    break
            else:
                break

############################################
# 좌상하 좌상상 우상상 우상하 좌하상 좌하하 우하하 우하상
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

for cy, cx in knights:
    for k in range(8):
        ny, nx = cy + dy[k], cx + dx[k]
        if 0 <= ny < n and 0 <= nx < m:
            if grid[ny][nx] != 2:
                grid[ny][nx] = 1

############################################
ans = 0
for row in grid:
    ans += row.count(0)

print(ans)
