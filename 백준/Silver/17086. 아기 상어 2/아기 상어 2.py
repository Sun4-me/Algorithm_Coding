# 이거 토마토 방식 응용해보자

from collections import deque
import sys

input = sys.stdin.readline

#  위 아 좌 우 위좌 위우 아좌 아우
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]


def bfs():
    while q:
        cur_y, cur_x = q.popleft()

        for d in range(8):
            ny, nx = cur_y + dy[d], cur_x + dx[d]
            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx] == 0:
                    grid[ny][nx] = grid[cur_y][cur_x] + 1
                    q.append((ny, nx))


##############################
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
##############################
# 아기 상어 위치 찾아서 q에 넣기
q = deque()
for row in range(n):
    for col in range(m):
        if grid[row][col] == 1:
            q.append((row, col))
##############################
bfs()
##############################
# 최대값 찾기
res = 0
for row in grid:
    res = max(res, max(row))

print(res - 1)
