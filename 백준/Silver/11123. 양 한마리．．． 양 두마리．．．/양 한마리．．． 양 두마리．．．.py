from collections import deque


def bfs(y, x):
    q = deque([(y, x)])
    v[y][x] = 1

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx] == "#":
                    if v[ny][nx] == 0:
                        v[ny][nx] = 1
                        q.append((ny, nx))


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    v = [[0] * m for _ in range(n)]

    ans = 0

    for y in range(n):
        for x in range(m):
            if grid[y][x] == "#" and v[y][x] == 0:
                ans += 1
                bfs(y, x)

    print(ans)
