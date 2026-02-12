# 상 우 하 좌
import sys

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def can_move(ny, nx):
    if 0 <= ny < n and 0 <= nx < m:
        if grid[ny][nx] != 'C':
            return True
    return False


##################################################
n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
sy, sx = map(int, input().split())
sy, sx = sy - 1, sx - 1
##################################################
max_time = 0
max_direct = ''

# 상 우 하 좌
# 0 1 2 3

direct = ['U', 'R', 'D', 'L']
for k in range(4):
    cy, cx = sy, sx
    d = k
    time = 1
    while True:
        ny, nx = cy + dy[d], cx + dx[d]

        if not can_move(ny, nx):
            break

        if time > n * m * 4:
            print(direct[k])
            print("Voyager")
            sys.exit()

        if grid[ny][nx] == '/':
            if d == 0:
                d = 1

            elif d == 1:
                d = 0

            elif d == 2:
                d = 3

            elif d == 3:
                d = 2

        elif grid[ny][nx] == '\\':
            if d == 0:
                d = 3

            elif d == 1:
                d = 2

            elif d == 2:
                d = 1

            elif d == 3:
                d = 0

        time += 1
        cy, cx = ny, nx

    if time > max_time:
        max_time = time
        max_direct = k

print(direct[max_direct])
print(max_time)
