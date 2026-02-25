import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def inb(y, x):
    return 0 <= y < n and 0 <= x < m


def melt(y, x):
    cnt = 0

    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if inb(ny, nx):
            if grid[ny][nx] == 0:
                cnt += 1

    val = max(0, grid[y][x] - cnt)

    if val == 0:
        remove_coord.append((y, x))

    melt_lst.append((y, x, val))


def bfs(y, x):
    q = deque([(y, x)])
    v[y][x] = 1

    while q:
        cy, cx = q.popleft()

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if inb(ny, nx):
                if grid[ny][nx] != 0 and v[ny][nx] == 0:
                    v[ny][nx] = 1
                    q.append((ny, nx))


#############################################################
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
#############################################################
# 빙산 좌표 찾기
coord = set()

for y in range(1, n - 1):
    for x in range(1, m - 1):
        if grid[y][x] != 0:
            coord.add((y, x))
#############################################################
if sum(sum(row) for row in grid) == 0:
    print(0)
    sys.exit()
#############################################################

time = 0

while True:
    v = [[0] * m for _ in range(n)]
    now_bing = 0

    time += 1

    remove_coord = []  #
    melt_lst = []  # 녹일 빙산

    for y, x in coord:
        melt(y, x)

    # 빙산 동시에 녹이기
    while melt_lst:
        y, x, val = melt_lst.pop()
        grid[y][x] = val

    for y, x in remove_coord:
        coord.remove((y, x))

    # 빙산이 없다면
    if not coord:
        print(0)
        sys.exit()

    for y, x in coord:
        if v[y][x] == 0:
            now_bing += 1
            bfs(y, x)

    if now_bing >= 2:
        break

print(time)
