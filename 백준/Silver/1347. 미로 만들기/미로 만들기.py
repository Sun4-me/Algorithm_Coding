# 하, 서, 상, 우
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def turn_right(d):
    return (d + 1) % 4


def turn_left(d):
    return (d - 1) % 4


def front(cy, cx, d):
    return cy + dy[d], cx + dx[d]


n = int(input())
command = list(input())

cy, cx, cd = 0, 0, 0
v_set = set()
v_set.add((cy, cx))

min_x, max_x, min_y, max_y = 0, 0, 0, 0

for cmd in command:
    if cmd == 'R':
        cd = turn_right(cd)

    elif cmd == 'L':
        cd = turn_left(cd)

    elif cmd == 'F':
        cy, cx = front(cy, cx, cd)
        v_set.add((cy, cx))
        min_x = min(min_x, cx)
        max_x = max(max_x, cx)
        min_y = min(min_y, cy)
        max_y = max(max_y, cy)

grid = [["#"] * abs(max_x - min_x + 1) for _ in range(abs(max_y - min_y + 1))]

y_offset = min_y
x_offset = min_x

for y, x in v_set:
    grid[y - y_offset][x - x_offset] = '.'

for row in grid:
    print(*row, sep="")
