from collections import deque
import sys

input = sys.stdin.readline


##############################################################
def bfs(y, x):
    grid[y][x] = 1
    q = deque([(y, x)])

    while q:
        cy, cx = q.popleft()

        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx] == 1:
                    grid[ny][nx] = grid[cy][cx] + 1
                    q.append((ny, nx))


##############################################################
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
##############################################################
# 구상
# 목표지점만 따로 저장. 목표지점부터 1로 시작.
# 최종 결과에서 목표지점 이외에 1인 지점은 -1
# 0은 그대로 두면 됨 갈수 없는 땅이니
# v 쓰지말고 grid 쓰자
##############################################################
# 목표지점 찾기
target_y, target_x = 0, 0
for row in range(n):
    for col in range(m):
        if grid[row][col] == 2:
            target_y, target_x = row, col
##############################################################
bfs(target_y, target_x)
##############################################################
# 정답 후처리
for row in range(n):
    for col in range(m):
        if grid[row][col] > 1:
            grid[row][col] -= 1
        elif grid[row][col] == 1:
            grid[row][col] = -1

grid[target_y][target_x] = 0

for row in grid:
    print(*row)
