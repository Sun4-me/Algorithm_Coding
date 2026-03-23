from collections import deque

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

start_a = (-1, -1)
start_b = (-1, -1)

for y in range(N):
    for x in range(M):
        if grid[y][x] == 'A':
            start_a = (y, x)
        elif grid[y][x] == 'B':
            start_b = (y, x)

dr = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1, 0]

v = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

q = deque()
q.append((start_a[0], start_a[1], start_b[0], start_b[1], 0))
v[start_a[0]][start_a[1]][start_b[0]][start_b[1]] = True

ans = -1

while q:
    ay, ax, by, bx, turns = q.popleft()

    if ay == start_b[0] and ax == start_b[1] and by == start_a[0] and bx == start_a[1]:
        ans = turns
        break

    for y in range(9):
        nay = ay + dr[y]
        nax = ax + dc[y]

        if not (0 <= nay < N and 0 <= nax < M) or grid[nay][nax] == 'X':
            continue

        for x in range(9):
            nby = by + dr[x]
            nbx = bx + dc[x]

            if not (0 <= nby < N and 0 <= nbx < M) or grid[nby][nbx] == 'X':
                continue

            # 턴이 끝났을 때 두 플레이어가 같은 위치에 있으면 안 됨
            if nay == nby and nax == nbx:
                continue

            # 두 플레이어가 서로 교차해서 자리를 맞바꾸면 안 됨
            if nay == by and nax == bx and nby == ay and nbx == ax:
                continue

            # 아직 방문하지 않은 상태여야 함
            if not v[nay][nax][nby][nbx]:
                v[nay][nax][nby][nbx] = True
                q.append((nay, nax, nby, nbx, turns + 1))

print(ans)
