# import sys
from collections import deque


from pprint import *


# 전치하고 리버스해서 첫 열만 확인하자
# 매 사이클 첫 열만 확인, 방문 초기화
# 방문이 안된 색깔 있는 좌표만 탐색
# 해당 행에 append 빈칸 수행하고. pop 할 색깔들 큰것 부터 pop

def bfs(cy, cx, color):
    global now_cnt, ans, flag
    v[cy][cx] = 1
    q = deque([(cy, cx)])

    ###########################
    now_pop = []
    now_pop.append((cy, cx))
    ###########################

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < 6 and 0 <= nx < 12:
                if v[ny][nx] == 0:
                    if grid[ny][nx] == color:
                        v[ny][nx] = 1
                        now_cnt += 1  # 방문 수 카운트
                        now_pop.append((ny, nx))  # 지울 좌표 +
                        q.append((ny, nx))

    # 4번이상인 경우에만 전역 변수에 업데이트
    if now_cnt >= 4:
        pop_cord.extend(now_pop)
        flag = True


############################################################
original_grid = [list(input()) for _ in range(12)]
# 전치 + reverse
grid = [lst[::-1] for lst in list(map(list, zip(*original_grid)))]
############################################################
ans = 0
count = 0

while True:
    if count == 30:
        break

    count += 1

    # 지울 좌표 목록
    pop_cord = []

    # 이번 턴에 성공
    flag = False

    v = [[0] * 12 for _ in range(6)]

    for row_idx in range(6):
        for col_idx in range(12):
            now_cnt = 1
            if grid[row_idx][col_idx] != '.':
                if v[row_idx][col_idx] == 0:
                    color = grid[row_idx][col_idx]
                    bfs(row_idx, col_idx, color)

    # x가 큰거 부터 지워야 한다
    pop_cord.sort(key=lambda x: -x[1])

    for y, x in pop_cord:
        grid[y].pop(x)
        grid[y].append('.')

    if flag:
        ans += 1
############################################################
print(ans)
