import sys

# 0: 우 1: 하 2: 좌 3: 상
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


def inb(y, x):
    return 0 <= y < m and 0 <= x < m


def turn(d, change):
    if change == 1:
        d = (d + 1) % 4
    elif change == 0:
        d = (d - 1) % 4

    return d


def move(cy, cx, d, step):
    ny, nx = cy + (step * dy[d]), cx + (step * dx[d])

    if not inb(ny, nx):
        print(-1)
        sys.exit()

    return ny, nx


#################################################
# 한 변의 길이, 수행할 명령어 수
m, n = map(int, input().split())
command = [list(input().split()) for _ in range(n)]
#################################################
cy, cx, d = 0, 0, 0

for cmd in command:
    if cmd[0] == "MOVE":
        cy, cx = move(cy, cx, d, int(cmd[1]))
    else:
        d = turn(d, int(cmd[1]))

print(cx, cy)