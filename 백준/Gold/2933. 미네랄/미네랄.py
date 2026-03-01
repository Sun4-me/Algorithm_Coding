from collections import deque


def bfs(y, x):
    q = deque([(y, x)])
    v[y][x] = 1

    coord = set()
    coord.add((y, x))

    max_y = 10 ** 10
    min_y = R - y - 1

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < R and 0 <= nx < C:
                if grid[ny][nx] == 'x':
                    if v[ny][nx] == 0:
                        v[ny][nx] = 1
                        min_y = min(min_y, R - ny - 1)
                        coord.add((ny, nx))
                        q.append((ny, nx))

    if min_y > 0:
        for y, x in coord:
            max_y = min(max_y, find_h(coord, y, x))

        for y, x in coord:
            grid[y][x] = '.'

        for y, x in coord:
            grid[y + max_y][x] = 'x'

        


def find_h(coord, y, x):
    h = 0

    for j in range(1, R):
        if 0 <= y + j < R:
            if not (y + j, x) in coord and grid[y + j][x] == 'x':
                break
            h += 1
        else:
            break

    return h


#############################################
R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
N = int(input())
height = list(map(int, input().split()))
#############################################
dir = 0  # 오른쪽

for h in height:

    if dir == 0:
        dir = (dir + 1) % 2

        for i in range(C):
            if grid[R - h][i] == 'x':
                grid[R - h][i] = '.'
                cy, cx = R - h, i
                break
        else:
            continue

    elif dir == 1:
        dir = (dir + 1) % 2

        for i in range(C - 1, -1, -1):
            if grid[R - h][i] == 'x':
                grid[R - h][i] = '.'
                cy, cx = R - h, i
                break
        else:
            continue

    v = [[0] * C for _ in range(R)]

    for dy, dx in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < R and 0 <= nx < C:
            if grid[ny][nx] == 'x':
                if v[ny][nx] == 0:
                    bfs(ny, nx)

for row in grid:
    print(*row, sep="")
