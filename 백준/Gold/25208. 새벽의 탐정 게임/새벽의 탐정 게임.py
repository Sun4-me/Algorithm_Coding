import sys
from collections import deque

# 우, 하, 좌, 상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def rotate_dice(q1, q2, d):
    if d == 0:
        nq1 = (q1[3], q1[0], q1[1], q1[2])
        nq2 = (nq1[0], q2[1], nq1[2], q2[3])
    elif d == 1:
        nq2 = (q2[3], q2[0], q2[1], q2[2])
        nq1 = (nq2[0], q1[1], nq2[2], q1[3])
    elif d == 2:
        nq1 = (q1[1], q1[2], q1[3], q1[0])
        nq2 = (nq1[0], q2[1], nq1[2], q2[3])
    elif d == 3:
        nq2 = (q2[1], q2[2], q2[3], q2[0])
        nq1 = (nq2[0], q1[1], nq2[2], q1[3])

    return nq1, nq2


def bfs():
    q = deque([(sy, sx, (1, 3, 6, 4), (1, 5, 6, 2))])
    v = [[[[0] * 7 for _ in range(7)] for _ in range(M)] for _ in range(N)]
    v[sy][sx][6][3] = 1


    while q:
        cy, cx, q1, q2 = q.popleft()
        now_bottom = q1[2]
        now_front= q1[1]

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                nq1, nq2 = rotate_dice(q1, q2, k)
                nxt_bottom = nq1[2]
                nxt_front = nq1[1]

                if grid[ny][nx] != "#" and v[ny][nx][nxt_bottom][nxt_front] == 0:
                    if grid[ny][nx] == '.':
                        v[ny][nx][nxt_bottom][nxt_front] = v[cy][cx][now_bottom][now_front] + 1
                        q.append((ny, nx, nq1, nq2))

                    elif grid[ny][nx] == 'R':
                        if nxt_bottom == 6:
                            print(v[cy][cx][now_bottom][now_front])
                            sys.exit()

    print(-1)
    sys.exit()


##########################################################
input = sys.stdin.readline
N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]
##########################################################
sy, sx = 0, 0

for y in range(N):
    for x in range(M):
        if grid[y][x] == 'D':
            sy, sx = y, x
            grid[y][x] = '.'
            break
##########################################################
bfs()
