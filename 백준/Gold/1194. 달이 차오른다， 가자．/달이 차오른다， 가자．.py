from collections import deque


def bfs():
    v = [[{} for _ in range(M)] for _ in range(N)]
    v[sy][sx][(0,)] = 1
    q = deque([(sy, sx, (0,))])

    while q:
        cy, cx, c_key = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < M:
                if grid[ny][nx] == "#":
                    continue

                if grid[ny][nx] in ('a', 'b', 'c', 'd', 'e', 'f'):
                    if grid[ny][nx] not in c_key:
                        n_key = c_key + (grid[ny][nx],)
                        if n_key not in v[ny][nx].keys():
                            v[ny][nx][n_key] = v[cy][cx][c_key] + 1
                            q.append((ny, nx, n_key))

                    else:
                        if c_key not in v[ny][nx].keys():
                            v[ny][nx][c_key] = v[cy][cx][c_key] + 1
                            q.append((ny, nx, c_key))

                elif grid[ny][nx] in ('A', 'B', 'C', 'D', 'E', 'F'):
                    if grid[ny][nx].lower() in c_key:
                        if c_key not in v[ny][nx].keys():
                            v[ny][nx][c_key] = v[cy][cx][c_key] + 1
                            q.append((ny, nx, c_key))

                elif grid[ny][nx] == '.':
                    if c_key not in v[ny][nx].keys():
                        v[ny][nx][c_key] = v[cy][cx][c_key] + 1
                        q.append((ny, nx, c_key))

                elif grid[ny][nx] == '1':
                    return v[cy][cx][c_key]

    return -1


####################################################
N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
####################################################
end_coord = set()
sy, sx = 0, 0

for y in range(N):
    for x in range(M):
        if grid[y][x] == '0':
            sy, sx = y, x
            grid[y][x] = '.'
            break
####################################################
ans = bfs()
print(ans)
