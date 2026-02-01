from collections import deque


def bfs(y, x):
    q = deque([(y, x)])
    v[y][x] = 1
    cnt = 1  # 쓰레기 넓이

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if v[ny][nx] == 0 and grid[ny][nx] == 1:
                    v[ny][nx] = 1
                    cnt += 1
                    q.append((ny, nx))

    return cnt


#########################################################
n, m, k = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(k)]
#########################################################
# 쓰레기 1 표시
grid = [[0] * m for _ in range(n)]
for node in nodes:
    y, x = node[0] - 1, node[1] - 1
    grid[y][x] = 1
#########################################################
v = [[0] * m for _ in range(n)]  # 방문
res = []  # 쓰레기 넓이 담을 공간
for row in range(n):
    for col in range(m):
        if grid[row][col] == 1 and v[row][col] == 0:
            res.append(bfs(row, col))
#########################################################
print(max(res))
