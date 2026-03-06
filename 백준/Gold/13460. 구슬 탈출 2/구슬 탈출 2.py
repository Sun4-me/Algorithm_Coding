from collections import deque

# 우 하 좌 상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def inb(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs():
    v = dict()
    v[(ry, rx, by, bx)] = 1

    q = deque([(ry, rx, by, bx)])
    count = 0

    while q:
        cry, crx, cby, cbx = q.popleft()

        if v[(cry, crx, cby, cbx)] == 11:
            return -1

        for k in range(4):
            # 블루가 들어가는 경우
            if can_goal(cby, cbx, k):
                continue

            # 레드가 들어가는 경우
            if can_goal(cry, crx, k):
                return v[(cry, crx, cby, cbx)]

            nry, nrx, r_cnt = move_ball(cry, crx, k)
            nby, nbx, b_cnt = move_ball(cby, cbx, k)

            # 움직였는데 같은 위치라면 처리
            if (nry, nrx) == (nby, nbx):
                if r_cnt < b_cnt:
                    nby, nbx = nby - dy[k], nbx - dx[k]

                elif r_cnt > b_cnt:
                    nry, nrx = nry - dy[k], nrx - dx[k]

            if (nry, nrx, nby, nbx) not in v.keys():
                v[(nry, nrx, nby, nbx)] = v[(cry, crx, cby, cbx)] + 1
                count += 1
                q.append((nry, nrx, nby, nbx))

    return -1


def move_ball(y, x, k):
    """도착 좌표와 cnt 리턴"""
    cnt = 0
    cy, cx = y, x
    while True:
        ny, nx = cy + dy[k], cx + dx[k]

        if grid[ny][nx] == "#":
            break

        cy, cx, = ny, nx
        cnt += 1

    return cy, cx, cnt


def can_goal(y, x, k):
    """구멍으로 들어갈 수 있는가"""
    cy, cx = y, x
    while True:
        ny, nx = cy + dy[k], cx + dx[k]

        if grid[ny][nx] == "#":
            break

        if grid[ny][nx] == 'O':
            return True

        cy, cx, = ny, nx

    return False


#############################################
N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
#############################################
# 레드, 블루, 엔드 지점 확인

ry, rx, by, bx, ey, ex = 0, 0, 0, 0, 0, 0

for y in range(N):
    for x in range(M):
        if grid[y][x] == 'R':
            ry, rx = y, x
            grid[y][x] = '.'

        elif grid[y][x] == 'B':
            by, bx = y, x
            grid[y][x] = '.'

        elif grid[y][x] == 'O':
            ey, ex = y, x
#############################################
ans = bfs()
print(ans)
