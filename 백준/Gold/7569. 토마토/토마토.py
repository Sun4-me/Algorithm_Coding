from collections import deque

#  위 아래 왼쪽 오른쪽 앞 뒤
dx = [0, 0, -1, +1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]


def bfs():
    while q:
        cur_z, cur_y, cur_x = q.popleft()

        for direct in range(6):
            nz, ny, nx = cur_z + dz[direct], cur_y + dy[direct], cur_x + dx[direct]
            if 0 <= ny < n and 0 <= nx < m and 0 <= nz < h:
                if grid[nz][ny][nx] == 0:
                    grid[nz][ny][nx] = grid[cur_z][cur_y][cur_x] + 1
                    q.append((nz, ny, nx))


########################################
m, n, h = map(int, input().split())
grid = []
for _ in range(h):
    grid.append([list(map(int, input().split())) for _ in range(n)])
########################################
# 미리 다 넣어 놓기
q = deque()

for z in range(h):
    for row in range(n):
        for col in range(m):
            if grid[z][row][col] == 1:
                q.append((z, row, col))

bfs()
#################################################
# 토마토 익었는지 확인하자
res = 0
for z in range(h):
    for row in range(n):
        for col in range(m):
            if grid[z][row][col] == 0:
                print(-1)
                exit()
            res = max(res, grid[z][row][col])

print(res - 1)
