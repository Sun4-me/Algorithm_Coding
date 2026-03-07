from collections import deque


def bfs():
    v = [[{} for _ in range(M)] for _ in range(N)]
    
    start_key = frozenset()
    v[sy][sx][start_key] = 1
    q = deque([(sy, sx, start_key)])

    while q:
        cy, cx, c_key = q.popleft()

        if grid[cy][cx] == '1':
            return v[cy][cx][c_key] - 1

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx

            if 0 <= ny < N and 0 <= nx < M and grid[ny][nx] != "#":
                char = grid[ny][nx]

                # 1. 열쇠를 만났을 때 ('a' ~ 'f')
                if char.islower():
                    n_key = c_key | frozenset([char])

                    if n_key not in v[ny][nx]:
                        v[ny][nx][n_key] = v[cy][cx][c_key] + 1
                        q.append((ny, nx, n_key))

                # 2. 문을 만났을 때 ('A' ~ 'F')
                elif char.isupper():
                    if char.lower() in c_key:
                        if c_key not in v[ny][nx]:
                            v[ny][nx][c_key] = v[cy][cx][c_key] + 1
                            q.append((ny, nx, c_key))

                # 3. 빈 공간('.')이나 출구('1')를 만났을 때
                else:
                    if c_key not in v[ny][nx]:
                        v[ny][nx][c_key] = v[cy][cx][c_key] + 1
                        q.append((ny, nx, c_key))

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
