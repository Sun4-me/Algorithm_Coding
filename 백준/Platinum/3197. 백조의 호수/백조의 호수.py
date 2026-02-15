import sys
from collections import deque
from pprint import *

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# 얼음 녹이고 다음 녹일 얼음의 경계를 저장
def melt():
    while water_q:
        cy, cx = water_q.popleft()

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < r and 0 <= nx < c:
                if grid[ny][nx] == 'X':
                    grid[ny][nx] = '.'
                    next_water_q.append((ny, nx))


def move():
    while swan_q:
        cy, cx = swan_q.popleft()
        if (cy, cx) == (t_y, t_x):
            return True

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < r and 0 <= nx < c:
                if not v[ny][nx]:
                    v[ny][nx] = True
                    if grid[ny][nx] == 'X':
                        next_swan_q.append((ny, nx))
                    else:
                        swan_q.append((ny, nx))

    return False


###############################################################
r, c = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(r)]
swans = []
water_q = deque()
###############################################################
for cy in range(r):
    for cx in range(c):
        if grid[cy][cx] == 'L':
            swans.append((cy, cx))
            water_q.append((cy, cx))
        elif grid[cy][cx] == '.':
            water_q.append((cy, cx))
###############################################################
v = [[False] * c for _ in range(r)]

s_y, s_x = swans[0]
t_y, t_x = swans[1]

swan_q = deque([(s_y, s_x)])
v[s_y][s_x] = True
###############################################################
days = 0
while True:
    next_swan_q = deque()
    next_water_q = deque()

    if move():
        break

    melt()

    swan_q = next_swan_q
    water_q = next_water_q
    days += 1

print(days)
