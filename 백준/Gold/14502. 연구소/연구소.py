from collections import deque
from itertools import combinations
# from pprint import *
# 모든 경우의 수 로 벽 3개 다 그려보고
# 그때마다 2 위치 넣어둔 큐 넣고 돌려보고 최대값 갱신

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    while q:
        cy, cx = q.popleft()

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if v[ny][nx] == 0 and grid[ny][nx] == 0:
                    v[ny][nx] = 1
                    grid[ny][nx] = 2
                    q.append((ny, nx))


#############################################################################
n, m = map(int, input().split())
ori_grid = [list(map(int, input().split())) for _ in range(n)]
#############################################################################
coords = [(y, x) for x in range(m) for y in range(n) if ori_grid[y][x] == 0]
can_wall = list(combinations(coords, 3))
#############################################################################
virus = []

for y in range(n):
    for x in range(m):
        if ori_grid[y][x] == 2:
            virus.append((y, x))

#############################################################################
ans = 0
for wall in can_wall:
    cnt = 0

    grid = [lst[:] for lst in ori_grid]

    for i in range(3):
        grid[wall[i][0]][wall[i][1]] = 1

    q = deque(virus)
    v = [[0] * m for _ in range(n)]

    for y, x in virus:
        v[y][x] = 1

    bfs()

    for row in range(n):
        for col in range(m):
            if grid[row][col] == 0:
                cnt += 1

    ans = max(ans, cnt)
#############################################################################
print(ans)
