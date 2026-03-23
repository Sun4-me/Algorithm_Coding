import sys
from itertools import combinations
from collections import deque


def bfs():
    global ans

    cnt = 0

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                if grid[ny][nx] != 1:
                    if v[ny][nx] == 0:
                        v[ny][nx] = v[cy][cx] + 1
                        q.append((ny, nx))
                        if grid[ny][nx] == 0:
                            cnt += 1
                            if cnt == space_cnt:
                                ans = min(ans, v[cy][cx])
                                break


###############################################################
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
###############################################################
coord = [(y, x) for y in range(N) for x in range(N) if grid[y][x] == 2]
possible = [combi for combi in combinations(coord, M)]
space_cnt = 0
for y in range(N):
    for x in range(N):
        if grid[y][x] == 0:
            space_cnt += 1
###############################################################
if space_cnt == 0:
    print(0)
    sys.exit()
###############################################################
ans = 10 ** 10

for case in possible:
    v = [[0] * N for _ in range(N)]
    q = deque()
    for y, x in case:
        v[y][x] = 1
        q.append((y, x))

    bfs()
###############################################################
if ans == 10 ** 10:
    ans = -1

print(ans)