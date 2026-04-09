import sys
from collections import deque

# 동서남북
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def inb(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs():
    v = [[[0] * 4 for _ in range(M)] for _ in range(N)]
    v[sy][sx][sd] = 1

    q = deque([(sy, sx, sd, 1)])

    while q:
        cy, cx, cd, cnt = q.popleft()

        if (cy, cx, cd) == (ey, ex, ed):
            return v[cy][cx][ed] - 1

        for k in range(4):
            if cd == k:
                nxt_cnt = cnt

            elif cd ^ 1 == k:
                continue

            else:
                nxt_cnt = cnt + 1

            if v[cy][cx][k] == 0:
                v[cy][cx][k] = nxt_cnt
                q.append((cy, cx, k, nxt_cnt))

        for w in range(1, 4):
            ny, nx = cy + (dy[cd] * w), cx + (dx[cd] * w)

            if not inb(ny, nx):
                break

            if grid[ny][nx] == 1:
                break

            if v[ny][nx][cd] == 0:
                v[ny][nx][cd] = cnt + 1
                q.append((ny, nx, cd, cnt + 1))


#############################################################
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
sy, sx, sd = map(lambda x: int(x) - 1, input().split())
ey, ex, ed = map(lambda x: int(x) - 1, input().split())
#############################################################
ans = bfs()
print(ans)
