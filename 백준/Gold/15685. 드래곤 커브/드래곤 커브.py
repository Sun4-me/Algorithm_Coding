dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


def make_dragon(cy, cx, cd, g):
    lst = [(cy, cx), (cy + dy[cd], cx + dx[cd])]
    make_step = g

    first_y, first_x = cy, cx
    end_y, end_x = cy + dy[cd], cx + dx[cd]

    while make_step:

        nxt_diff = []

        for i in range(len(lst)):
            y, x = lst[i][0], lst[i][1]
            nxt_diff.append((x - end_x, -y + end_y))

            if (y, x) == (first_y, first_x):
                idx = i

        # 90도 회전하고 끝점만큼 더하기
        # nxt_diff = [(x - end_x, -y + end_y) for y, x in lst]

        for j in range(len(nxt_diff)):
            ddy, ddx = nxt_diff[j][0], nxt_diff[j][1]

            if (ddy, ddx) == (0, 0):
                continue

            lst.append((end_y + ddy, end_x + ddx))

            if j == idx:
                nxt_end_y, nxt_end_x = end_y + ddy, end_x + ddx

        make_step -= 1
        end_y, end_x = nxt_end_y, nxt_end_x

    return lst


def find_sqaure(y, x):
    if (y, x) not in coord:
        return False

    if (y + 1, x) not in coord:
        return False

    if (y, x + 1) not in coord:
        return False

    if (y + 1, x + 1) not in coord:
        return False

    return True


###########################################
N = int(input())
command = [list(map(int, input().split())) for _ in range(N)]
###########################################
coord = []

for cmd in command:
    x, y, d, g = cmd[0], cmd[1], cmd[2], cmd[3]
    lst = make_dragon(y, x, d, g)

    coord.extend(lst)

coord = set(coord)
###########################################
ans = 0

for y in range(101):
    for x in range(101):
        if find_sqaure(y, x):
            ans += 1

print(ans)
