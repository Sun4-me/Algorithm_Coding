from collections import deque
import sys

input = sys.stdin.readline

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
#################################################
m, n, h = map(int, input().split())
grid = []
for _ in range(h):
    grid.append([list(map(int, input().split())) for _ in range(n)])
#################################################
q = deque()

for depth in range(h):
    for row in range(n):
        for col in range(m):
            if grid[depth][row][col] == 1:
                q.append((depth, row, col))
#################################################
bfs()
#################################################
# 토마토가 모두 익었는지 확인
res = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if grid[i][j][k] == 0:
                print(-1)
                exit()
            res = max(res, grid[i][j][k])

print(res - 1)
