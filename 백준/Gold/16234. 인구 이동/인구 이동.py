from collections import deque


def inb(y, x):
    return 0 <= y < N and 0 <= x < N


def valid_diff(a, b):
    """연합을 이루는 차이인가"""
    return L <= abs(a - b) <= R


def marking(tot, cnt, st):
    """인구 이동 후 갱신"""
    mark_num = tot // cnt
    for y, x in st:
        grid[y][x] = mark_num


def bfs(y, x):
    q = deque([(y, x)])
    v[y][x] = 1

    total = grid[y][x]  # 연합의 인구수
    cnt = 1  # 연합을 이루는 칸의 개수
    coord = set()  # 연합을 이루는 좌표들
    coord.add((y, x))

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if inb(ny, nx):
                if v[ny][nx] == 0:
                    if valid_diff(grid[cy][cx], grid[ny][nx]):
                        v[ny][nx] = 1
                        total += grid[ny][nx]
                        cnt += 1
                        coord.add((ny, nx))
                        q.append((ny, nx))

    if cnt > 1:
        marking(total, cnt, coord)


###########################################################
N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
###########################################################
time = 0

while True:
    time += 1
    v = [[0] * N for _ in range(N)]

    cnt = 0
    for y in range(N):
        for x in range(N):
            if v[y][x] == 0:
                cnt += 1
                bfs(y, x)

    if cnt == (N * N):
        break

print(time - 1)
