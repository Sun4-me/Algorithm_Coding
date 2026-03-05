# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def inb(y, x):
    return 0 <= y < N and 0 <= x < N


def move(y, x, d):
    now_num = grid[y][x]
    rd = (d + 2) % 4
    flag = False  # 같은 숫자를 만난 경우 True

    # [1] 반대 방향으로 같은 숫자 탐색.
    # 다른 숫자 만나면 종료
    cy, cx = y, x

    while True:
        ny, nx = cy + dy[rd], cx + dx[rd]

        if not inb(ny, nx):
            break

        # 같은 숫자를 만났다면
        if grid[ny][nx] == now_num:
            # 두 위치는 각각 0으로 초기화 해두기
            grid[y][x] = 0
            grid[ny][nx] = 0

            # 마킹해둘 값
            now_num *= 2
            flag = True
            break

        elif grid[ny][nx] != 0:
            break

        cy, cx = ny, nx

    # 같은 숫자를 만나지 못했다면
    if not flag:
        # 현재 위치 초기화 해두기
        grid[y][x] = 0

    # [2] 현재 방향으로 최대한 보내주기
    if d == 0:
        cy, cx = 0, x
    elif d == 1:
        cy, cx = y, N - 1
    elif d == 2:
        cy, cx = N - 1, x
    elif d == 3:
        cy, cx = y, 0

    while True:
        if grid[cy][cx] == 0:
            grid[cy][cx] = now_num
            break

        cy, cx = cy + dy[rd], cx + dx[rd]

        if not inb(cy, cx):
            break


def back(depth, lst):
    if depth == 5:
        possible.append(lst)
        return

    for i in range(4):
        back(depth + 1, lst + [i])


#############################################################
N = int(input())
ori_grid = [list(map(int, input().split())) for _ in range(N)]
#############################################################
# 가능한 모든 방향 경우의 수
possible = []
back(0, [])

ans = 0

for case in possible:
    grid = [lst[:] for lst in ori_grid]

    for d in case:
        # 상
        if d == 0:
            for x in range(N):
                for y in range(N):
                    if grid[y][x] != 0:
                        move(y, x, d)

        # 우
        elif d == 1:
            for y in range(N):
                for x in range(N - 1, -1, -1):
                    if grid[y][x] != 0:
                        move(y, x, d)

        # 하
        elif d == 2:
            for x in range(N):
                for y in range(N - 1, -1, -1):
                    if grid[y][x] != 0:
                        move(y, x, d)

        # 좌
        elif d == 3:
            for y in range(N):
                for x in range(N):
                    if grid[y][x] != 0:
                        move(y, x, d)

    now_max = max(max(row) for row in grid)
    ans = max(ans, now_max)

print(ans)
