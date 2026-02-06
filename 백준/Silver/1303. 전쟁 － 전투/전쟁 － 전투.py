from collections import deque


def bfs(y, x, color):
    global white, blue
    v[y][x] = 1
    q = deque([(y, x)])
    cnt = 1

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < m and 0 <= nx < n:
                if v[ny][nx] == 0 and grid[ny][nx] == color:
                    v[ny][nx] = 1
                    cnt += 1
                    q.append((ny, nx))

    if color == "W":
        white += cnt ** 2
    else:
        blue += cnt ** 2


n, m = map(int, input().split())
# 가로 세로
# 우리병사 W, 적국 B, 모인만큼 N제곱의 위력
grid = [list(input()) for _ in range(m)]
v = [[0] * n for _ in range(m)]
#######################################
white = 0
blue = 0
#######################################
for row in range(m):
    for col in range(n):
        if v[row][col] == 0:
            color = grid[row][col]
            bfs(row, col, color)

print(white, blue)
