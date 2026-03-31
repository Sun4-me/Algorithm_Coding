from collections import deque


def bfs(y, x):
    global game
    v[y][x] = True
    q = deque([(y, x)])
    ttemp = [(y, x)]

    while q:
        cy, cx = q.popleft()
        cnum = grid[cy][cx]

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < N and 0 <= nx < M): continue
            if v[ny][nx]: continue
            if grid[ny][nx] == cnum:
                v[ny][nx] = True
                q.append((ny, nx))
                ttemp.append((ny, nx))

    if len(ttemp) >= 4:
        game = True
        coord.extend(ttemp)


tmp = [list(input()) for _ in range(12)]
grid = [lst[::-1] for lst in list(map(list, zip(*tmp)))]
N, M = 6, 12
ans = 0

while True:
    game = False

    v = [[False] * M for _ in range(N)]
    coord = []

    for y in range(N):
        for x in range(M):
            if grid[y][x] != '.' and not v[y][x]:
                bfs(y, x)

    for y, x in coord:
        grid[y][x] = '.'

    nxt_grid = [[] for _ in range(N)]

    for y in range(N):
        temp = []
        space_cnt = 0
        for x in range(M):
            if grid[y][x] == '.':
                space_cnt += 1
            else:
                temp.append(grid[y][x])

        for _ in range(space_cnt):
            temp.append('.')

        nxt_grid[y].extend(temp)

    if not game: break
    ans += 1

    grid = nxt_grid

print(ans)
