# 문제를 잘 읽자.
# 코드를 잘 치자.
# 유형 파악을 잘 하자.

# 1번 한쪽 방향 | 4가지
# 2번 반대 방향 | 2가지
# 3번 직각 방향 | 4가지
# 4번 세 방향   | 4가지
# 5번 네 방향   | 1가지

direction = [
    [],
    [[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]],
    [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],
    [[(-1, 0), (0, 1)], [(-1, 0), (0, -1)], [(1, 0), (0, -1)], [(1, 0), (0, 1)]],
    [[(-1, 0), (0, 1), (0, -1)], [(-1, 0), (0, -1), (1, 0)], [(1, 0), (0, -1), (0, 1)], [(1, 0), (0, 1), (-1, 0)]],
    [[(-1, 0), (1, 0), (0, -1), (0, 1)]],
]


def inb(y, x):
    return 0 <= y < N and 0 <= x < M


# def back(depth, i):
#     global ans
#
#     if depth == length:
#         now_sum = 0
#
#         for y in range(N):
#             for x in range(N):
#                 if grid[y][x] == '#':
#                     now_sum += 1
#
#         # if now_sum == 20:
#         for row in grid:
#             print(*row)
#
#         print()
#
#         ans = max(ans, now_sum)
#         return
#
#     cy, cx, num = coord[i][0], coord[i][1], coord[i][2]
#
#     if num in (1, 3, 4):
#         k = 4
#
#     elif num == 2:
#         k = 2
#
#     elif num == 5:
#         k = 1
#
#     for j in range(k):
#         mark(cy, cx, num, j, '#')
#         back(depth + 1, i + 1)
#         mark(cy, cx, num, j, 0)

def back(depth, s, lst):
    if depth == length:
        possible.append(lst)
        return

    for i in range(s, length):
        num = coord[i][2]

        if num in (1, 3, 4):
            k = 4

        elif num == 2:
            k = 2

        elif num == 5:
            k = 1

        for j in range(k):
            back(depth + 1, i + 1, lst + [j])


def mark(y, x, num, d, marking):
    for dy, dx in direction[num][d]:
        cy, cx = y, x
        while True:
            ny, nx = cy + dy, cx + dx
            if not inb(ny, nx):
                break

            if grid[ny][nx] == 6:
                break

            if grid[ny][nx] == 0:
                grid[ny][nx] = marking

            cy, cx = ny, nx


###############################################################
N, M = map(int, input().split())
ori_grid = [list(map(int, input().split())) for _ in range(N)]
###############################################################
total_size = N * M
coord = []

for y in range(N):
    for x in range(M):
        if ori_grid[y][x] != 0 and ori_grid[y][x] != 6:
            coord.append((y, x, ori_grid[y][x]))

        if ori_grid[y][x] == 6:
            total_size -= 1

length = len(coord)
total_size -= length
###############################################################
possible = []
back(0, 0, [])

ans = 0  # 감시하는 최대 영역

for lst in possible:
    grid = [arr[:] for arr in ori_grid]

    for i in range(length):
        cy, cx, num, d = coord[i][0], coord[i][1], coord[i][2], lst[i]
        mark(cy, cx, num, d, '#')

    now_sum = 0
    for y in range(N):
        for x in range(M):
            if grid[y][x] == '#':
                now_sum += 1

    ans = max(ans, now_sum)

# 사각 지대의 최소 크기
print(total_size - ans)
###############################
