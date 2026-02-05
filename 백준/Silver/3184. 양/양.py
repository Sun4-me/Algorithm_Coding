from collections import deque


def bfs(y, x):
    v[y][x] = 1
    q = deque([(y, x)])
    yang = 0
    wolf = 0
    if grid[y][x] == 'o':
        yang += 1
    elif grid[y][x] == 'v':
        wolf += 1

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < r and 0 <= nx < c:
                if grid[ny][nx] != '#' and v[ny][nx] == 0:
                    v[ny][nx] = 1
                    q.append((ny, nx))
                    if grid[ny][nx] == 'o':
                        yang += 1
                    elif grid[ny][nx] == 'v':
                        wolf += 1

    if yang > wolf:
        wolf = 0
    else:
        yang = 0

    return yang, wolf


r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
v = [[0] * c for _ in range(r)]

yang_cnt = 0
wolf_cnt = 0

for row in range(r):
    for col in range(c):
        if v[row][col] == 0 and grid[row][col] != '#':
            yc, wc = bfs(row, col)
            yang_cnt += yc
            wolf_cnt += wc

print(yang_cnt, wolf_cnt)
