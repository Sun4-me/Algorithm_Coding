# 불 2, 방화벽 1, 빈칸 0
# n, m 이 매우 작음 모든 경우 다 해보자
# 빈 칸인 경우에만 방화벽 설치가능

from itertools import combinations
from collections import deque


def bfs():
    cnt = fire_cnt

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx] == 0 and v[ny][nx] == 0:
                    grid[ny][nx] = 2
                    v[ny][nx] = 1
                    cnt += 1
                    q.append((ny, nx))

    return cnt


###########################################################
n, m = map(int, input().split())
ori_grid = [list(map(int, input().split())) for _ in range(n)]
###########################################################
# 빈칸인 좌표 모음
coords = [(y, x) for y in range(n) for x in range(m) if ori_grid[y][x] == 0]

# 가능한 3가지 좌표의 경우의 수
possible = list(combinations(coords, 3))
###########################################################
# 불 좌표 찾아 두기
# 빈칸 개수 찾아 두기
ori_v = [[0] * m for _ in range(n)]

fire = []
wall_cnt = 0

for y in range(n):
    for x in range(m):
        if ori_grid[y][x] == 2:
            fire.append((y, x))
            ori_v[y][x] = 1

        elif ori_grid[y][x] == 1:
            wall_cnt += 1

fire_cnt = len(fire)
###########################################################
min_cnt = 10 ** 10

for case in possible:
    # 임시 배열 생성 및 q,v 초기화
    v = [row[:] for row in ori_v]
    grid = [row[:] for row in ori_grid]
    q = deque(fire)

    # 벽 생성
    for i in range(3):
        now = case[i]
        now_y, now_x = now[0], now[1]
        grid[now_y][now_x] = 1

    # 불 퍼트리기
    cnt = bfs()

    # 불을 퍼트린 영역의 수 탐색 및 가장 적게 퍼트린 영역 저장
    min_cnt = min(min_cnt, cnt)

# 전체크기에서 불을 가장 적게 퍼트린 영역과 방화벽의수, 추가한 방화벽 3을 빼면
# 불이 퍼지지 않는 영역크기의 최댓값임.
print(n * m - (min_cnt + wall_cnt + 3))
