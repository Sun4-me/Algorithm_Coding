import sys
from pprint import *

# 0 1 2 3
# 하 좌 상 우
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


# 좀비는 벽 이면 턴.
# 아리는 벽 이면 노 행동

def inb(y, x):
    return 0 <= y < n and 0 <= x < n


def ari_move(cy, cx, d):
    ny, nx = cy + dy[d], cx + dx[d]

    if inb(ny, nx):
        if (ny, nx) in switches:
            switch_on(ny, nx)

        if grid[ny][nx] != 'Z' or (grid[ny][nx] == 'Z' and safe[ny][nx] == 1):
            grid[ny][nx] = 'A'
            grid[cy][cx] = 'O'
            return ny, nx
        else:
            print("Aaaaaah!")
            sys.exit()
    else:
        return cy, cx


# 좀비용
def zombi_move(cy, cx, d):
    ny, nx = cy + dy[d], cx + dx[d]

    if inb(ny, nx):
        if grid[ny][nx] == "A" and safe[ny][nx] == 0:
            print("Aaaaaah!")
            sys.exit()

        grid[ny][nx] = 'Z'
        grid[cy][cx] = 'O'
        return ny, nx, d

    return cy, cx, turn_aruound(d)


# 좀비용
def turn_aruound(d):
    if d == 0:
        return 2
    return 0


def left_turn(d):
    d = (d - 1) % 4
    return d


def right_turn(d):
    d = (d + 1) % 4
    return d


def switch_on(cy, cx):
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    safe[cy][cx] = 1
    for dy, dx in direct:
        ny, nx = cy + dy, cx + dx
        if inb(ny, nx):
            safe[ny][nx] = 1


n = int(input())
command = list(input())
grid = [list(input()) for _ in range(n)]
# z 학생, s 스위치, o 빈칸
cy, cx = 0, 0

safe = [[0] * n for _ in range(n)]
zombies = []
switches = []

grid[0][0] = "A"

for row in range(n):
    for col in range(n):
        if grid[row][col] == 'Z':
            zombies.append((row, col, 0))

        elif grid[row][col] == 'S':
            switches.append((row, col))

d = 0

for cmd in command:

    if cmd == "F":
        cy, cx = ari_move(cy, cx, d)

    elif cmd == "L":
        d = left_turn(d)

    elif cmd == "R":
        d = right_turn(d)

    for i in range(len(zombies)):
        zy, zx, zd = zombies[i]
        ny, nx, nd = zombi_move(zy, zx, zd)
        zombies[i] = (ny, nx, nd)

print("Phew...")
