import sys
from collections import deque

# --------------------------------------------
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def inb(y, x):
    return 0 <= y < N and 0 <= x < M


# --------------------------------------------

def find_coord():
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 3:
                by, bx = y, x

                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if not inb(ny, nx): continue
                    if grid[ny][nx] == 2:
                        ay, ax = ny, nx
                        return ay, ax, k, by, bx, k


# --------------------------------------------

def check():
    if b_hp <= 0:
        print("VICTORY!")
        sys.exit()
    elif a_hp <= 0:
        print("CAVELIFE...")
        sys.exit()


# --------------------------------------------

def ari_attack():
    global b_hp
    b_hp -= a_power


# --------------------------------------------

def ari_move():
    global ay, ax, ad, a_hp

    ny, nx = ay + dy[ad], ax + dx[ad]
    if inb(ny, nx) and grid[ny][nx] == 0:
        py, px = ay, ax
        grid[ay][ax] = 0
        ay, ax = ny, nx
        grid[ay][ax] = 2
        return True, py, px, ad

    for _ in range(4):
        a_hp -= 1
        ad = (ad + 1) % 4
        ny, nx = ay + dy[ad], ax + dx[ad]
        if inb(ny, nx) and grid[ny][nx] == 0:
            py, px = ay, ax
            grid[ay][ax] = 0
            ay, ax = ny, nx
            grid[ay][ax] = 2
            return True, py, px, ad

    return False, -1, -1, -1


# --------------------------------------------

def make_pattern():
    pattern = []
    coord = [(0, 0)]
    y, x, d = 0, 0, 0
    step = 0
    how = 1
    w = 1
    cnt = 0

    while True:
        if cnt == 10 ** 4 + 10: break
        y, x = y + dy[d], x + dx[d]
        coord.append((y, x))

        how -= 1
        cnt += 1

        if how == 0:
            d = (d + 1) % 4
            step += 1
            how = w
            if step == 2:
                step = 0
                w += 1
                how = w

    pattern.append(coord)

    for _ in range(3):
        nxt_coord = []
        for y, x in pattern[-1]:
            nxt_coord.append((x, -y))
        pattern.append(nxt_coord)
    return pattern


# --------------------------------------------

def boss_attack():
    if not son: return

    sy, sx = -1, -1
    for y, x in pattern[bd]:
        ny, nx = y + by, x + bx
        if not inb(ny, nx): continue
        if grid[ny][nx] == 1:
            sy, sx = ny, nx
            break

    bfs(sy, sx)


# --------------------------------------------
def bfs(sy, sx):
    global a_hp
    v = [[0] * M for _ in range(N)]
    v[sy][sx] = 1
    q = deque([(sy, sx)])

    while q:
        cy, cx = q.popleft()

        if (cy, cx) == (ay, ax):
            if b_power - (v[cy][cx] - 1) > 0:
                a_hp -= b_power - (v[cy][cx] - 1)
            return

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if not inb(ny, nx): continue
            if v[ny][nx]: continue
            if grid[ny][nx] in (0, 2):
                v[ny][nx] = v[cy][cx] + 1
                q.append((ny, nx))


# --------------------------------------------
def boss_move(yes_m, py, px, pd):
    global by, bx, bd
    if not yes_m: return
    grid[by][bx] = 0
    by, bx, bd = py, px, pd
    grid[by][bx] = 3


# --------------------------------------------
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
a_hp, a_power, b_hp, b_power = map(int, input().split())
# --------------------------------------------
ay, ax, ad, by, bx, bd = find_coord()
# --------------------------------------------
pattern = make_pattern()
# --------------------------------------------
son = True
if sum(sum(row) for row in grid) == 5:
    son = False
# --------------------------------------------
while True:
    ari_attack()
    check()
    yes_m, py, px, pd = ari_move()
    check()
    boss_attack()
    check()
    boss_move(yes_m, py, px, pd)
