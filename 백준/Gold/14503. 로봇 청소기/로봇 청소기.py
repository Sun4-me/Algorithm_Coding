# 0: 상, 1: 우, 2, 하, 3: 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def inb(ny, nx):
    return 0 <= ny < n and 0 <= nx < m


def check_clear(cy, cx):
    for k in range(4):
        ny, nx = cy + dy[k], cx + dx[k]
        if inb(ny, nx):
            if grid[ny][nx] == 0:
                return False
    return True


def walk(cy, cx):
    global cnt
    if grid[cy][cx] == 0:
        cnt += 1
        grid[cy][cx] = 2


def check_back(cy, cx, direct):
    k = (direct + 2) % 4
    ny, nx = cy + dy[k], cx + dx[k]

    if inb(ny, nx):
        if grid[ny][nx] == 2:
            return True

    return False


def go_back(cy, cx, direct):
    k = (direct + 2) % 4
    ny, nx = cy + dy[k], cx + dx[k]
    return ny, nx


def turn(direct):
    k = (direct - 1) % 4
    return k


def check_front(cy, cx, direct):
    ny, nx = cy + dy[direct], cx + dx[direct]
    if inb(ny, nx):
        if grid[ny][nx] == 0:
            return True
    return False


def go(cy, cx, direct):
    ny, nx = cy + dy[direct], cx + dx[direct]
    return ny, nx


# 2: 청소한 빈칸, 1: 벽, 0: 청소 되지 않은 빈칸
#################################################################
n, m = map(int, input().split())
r, c, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
#################################################################
cnt = 0

cy, cx, d = r, c, d
while True:
    walk(cy, cx)

    if check_clear(cy, cx):
        if check_back(cy, cx, d):
            cy, cx = go_back(cy, cx, d)
        else:
            break

    else:
        d = turn(d)
        if check_front(cy, cx, d):
            cy, cx = go(cy, cx, d)

print(cnt)