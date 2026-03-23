dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def inb(y, x):
    return 0 <= y < N and 0 <= x < N


def make_core():
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 1:

                direct = [True] * 4

                for k in range(4):
                    cy, cx = y, x

                    while True:
                        ny, nx = cy + dy[k], cx + dx[k]

                        if not inb(ny, nx):
                            break

                        if grid[ny][nx] == 1:
                            direct[k] = False
                            break

                        cy, cx = ny, nx

                if any(direct):
                    # 가장자리 pass
                    if y == 0 or x == 0 or y == N - 1 or x == N - 1:
                        continue
                    core.append((y, x))
                    core_direct.append(direct)


def can_go(y, x, k):
    cy, cx = y, x
    while True:
        cy, cx = cy + dy[k], cx + dx[k]

        if not inb(cy, cx):
            break

        if grid[cy][cx] == 1:
            return False

    return True


def masking(y, x, k, num):
    cy, cx = y, x
    w = 0
    while True:
        cy, cx = cy + dy[k], cx + dx[k]

        if not inb(cy, cx):
            break

        grid[cy][cx] = num
        w += 1

    return w


def dfs(depth, idx, cnt, sm):
    global max_cnt, min_length

    if depth == core_length:

        if cnt > max_cnt:
            max_cnt = cnt
            min_length = sm

        elif cnt == max_cnt:
            min_length = min(min_length, sm)

        return

    cy, cx = core[idx]

    # 연결 안하고 보내기
    dfs(depth + 1, idx + 1, cnt, sm)

    for i in range(4):
        if core_direct[idx][i]:
            # 갈 수 있다면 연결하고 보내기
            if can_go(cy, cx, i):
                w = masking(cy, cx, i, 1)
                dfs(depth + 1, idx + 1, cnt + 1, sm + w)
                masking(cy, cx, i, 0)


T = int(input())

for case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    core = []
    core_direct = []




    make_core()

    core_length = len(core)
    max_cnt = 0
    min_length = 10 ** 10

    dfs(0, 0, 0, 0)

    print(f"#{case} {min_length}")
