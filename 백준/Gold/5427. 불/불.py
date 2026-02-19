from collections import deque


def bfs():
    while q:
        cy, cx, who = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m:
                # 상근
                if who == 0:
                    if grid[ny][nx] == '.' and v_sang[ny][nx] == 0:
                        v_sang[ny][nx] = v_sang[cy][cx] + 1
                        q.append((ny, nx, 0))

                # 불
                elif who == 1:
                    if grid[ny][nx] != '#' and v_fire[ny][nx] == 0:
                        grid[ny][nx] = '*'
                        v_fire[ny][nx] = 1
                        q.append((ny, nx, 1))


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    v_fire = [[0] * m for _ in range(n)]
    v_sang = [[0] * m for _ in range(n)]

    # 상근 0, 불 1
    sy, sx, who = -1, -1, 0
    q = deque([])

    for y in range(n):
        for x in range(m):
            if grid[y][x] == '*':
                v_fire[y][x] = 1
                q.append((y, x, 1))

            elif grid[y][x] == '@':
                v_sang[y][x] = 1
                sy, sx = y, x

    q.append((sy, sx, who))

    bfs()

    # 테두리 확인
    min_time = 10 ** 10


    for x in range(m):

        if v_sang[0][x] != 0:
            min_time = min(min_time, v_sang[0][x])

        if v_sang[-1][x] != 0:
            min_time = min(min_time, v_sang[-1][x])

    for y in range(n):
        if v_sang[y][0] != 0:
            min_time = min(min_time, v_sang[y][0])

        if v_sang[y][-1] != 0:
            min_time = min(min_time, v_sang[y][-1])

    if min_time == 10 ** 10:
        print("IMPOSSIBLE")
    else:
        print(min_time)
