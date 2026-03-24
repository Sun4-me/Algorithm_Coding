import sys
from collections import deque


def inb(cy, cx):
    if not (0 <= cy < N and 0 <= cx < M):
        return False

    if not (0 <= cy + A - 1 < N and 0 <= cx < M):
        return False

    if not (0 <= cy < N and 0 <= cx + B - 1 < M):
        return False

    if not (0 <= cy < N + A - 1 and 0 <= cx + B - 1 < M):
        return False

    for y in range(cy, cy + A):
        for x in range(cx, cx + B):
            if grid[y][x] == 1:
                return False

    return True


def bfs(sy, sx):
    v = [[0] * M for _ in range(N)]
    v[sy][sx] = 1

    q = deque([(sy, sx)])

    while q:
        cy, cx = q.popleft()

        if (cy, cx) == (ey, ex):
            print(v[cy][cx] - 1)
            sys.exit()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx

            if not inb(ny, nx):
                continue

            if v[ny][nx] == 0:
                v[ny][nx] = v[cy][cx] + 1
                q.append((ny, nx))

    print(-1)
    sys.exit()


####################################################
N, M, A, B, K = map(int, input().split())
grid = [[0] * M for _ in range(N)]
for _ in range(K):
    y, x = map(lambda x: int(x) - 1, input().split())
    grid[y][x] = 1

sy, sx = map(lambda x: int(x) - 1, input().split())
ey, ex = map(lambda x: int(x) - 1, input().split())
####################################################
bfs(sy, sx)
