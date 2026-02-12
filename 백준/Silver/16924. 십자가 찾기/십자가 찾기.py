# 모든 별을 기준으로 상하좌우 별을 항상 최대 길이로 만들기
import sys
from pprint import *

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def inb(y, x):
    return 0 <= y < n and 0 <= x < m


def draw(cy, cx):
    global cnt
    for k in range(4):
        ny, nx = cy + dy[k], cx + dx[k]
        if not inb(ny, nx):
            return
        if grid[ny][nx] == '.':
            return

    size = 1
    flag = True

    while flag:
        for k in range(4):
            ny, nx = cy + (size * dy[k]), cx + (size * dx[k])
            if not inb(ny, nx):
                flag = False
                break
            if grid[ny][nx] == '.':
                flag = False
                break
        else:
            size += 1

    v[cy][cx] = '*'

    for i in range(1, size):
        for k in range(4):
            ny, nx = cy + (i * dy[k]), cx + (i * dx[k])
            v[ny][nx] = '*'

    cnt += 1
    res.append([cy + 1, cx + 1, size - 1])


###################################################
n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
###################################################
v = [[0] * m for _ in range(n)]
cnt = 0  # 필요한 십자가의 수
res = []  # 가능한 경우(x, y, s)
###################################################
# 탐색하면서 별 좌표도 같이 저장
stars = []
for row in range(n):
    for col in range(m):
        if grid[row][col] == '*':
            stars.append((row, col))
            draw(row, col)
###################################################
for row, col in stars:
    if not v[row][col] == '*':
        print(-1)
        sys.exit()
###################################################
print(cnt)
for i in res:
    print(*i)

