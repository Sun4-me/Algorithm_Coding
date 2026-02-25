import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def inb(y, x):
    return 0 <= y < n and 0 <= x < m


def bfs():
    while q:
        cy, cx, state = q.popleft()

        if state == 0 and (cy, cx, 1) in fires:
            continue

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if inb(ny, nx):
                if state == 0:
                    if (ny, nx) not in fires:
                        if grid[ny][nx] != '#':
                            if v[ny][nx] == 0:
                                v[ny][nx] = v[cy][cx] + 1
                                q.append((ny, nx, state))

                else:
                    if grid[ny][nx] != '#':
                        if fire_v[ny][nx] == 0:
                            fire_v[ny][nx] = 1
                            fires.add((ny, nx, state))
                            q.append((ny, nx, state))

            else:
                if state == 0:
                    print(v[cy][cx])
                    sys.exit()

    print("IMPOSSIBLE")
    sys.exit()


######################################
n, m = map(int, input().split())
grid = list(input() for _ in range(n))
######################################
v = [[0] * m for _ in range(n)]
fire_v = [[0] * m for _ in range(n)]

sy, sx = 0, 0
fires = set()

q = deque()

for y in range(n):
    for x in range(m):
        if grid[y][x] == 'F':
            fire_v[y][x] = 1
            fires.add((y, x, 1))
            q.append((y, x, 1))

        elif grid[y][x] == 'J':
            sy, sx = y, x
            v[y][x] = 1
            q.appendleft((sy, sx, 0))
######################################
bfs()
