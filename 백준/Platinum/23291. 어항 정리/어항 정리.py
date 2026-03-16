# [초기 정보]
# 상어가 가지고 있는 어항 N개
# 물고기가 한 마리 이상 있음

# [1번: 물고기 추가]
# 물고기의 수가 가장 적은 어항에 물고기 한 마리 넣기
# 작은 값이 여러개면 그 모두에 한 마리씩

# [2번: 어항 쌓고 돌리기]
# 1) 가장 왼쪽에 있는 어항을 그 오른쪽에 있는 어항 위에 올려놓기
# 2) 2개 이상 쌓여 있는 어항을 모두 공중 부양
# 3) 전체를 시계방향 90도 회전
# 4) 가장 왼쪽에 있는 어항 위에 공중 부양 시킨 어항 중 가장 왼쪽에 있는 어항 위치
# 공중 부양시킨 어항 중 가장 오른쪽에 있는 어항의 아래에
# 바닥에 있는 어항이 있을때까지 반복

# [3번: 물고기 수 조절]
# 1) 모든 인접한 두 어항에 대해서 물고기 수의 차이를 구함
# 2) 이 차이를 5로 나눈 몫을 d
# 4) d가 0보다 크면, 두 어항 중 물고기의 수가 많은 곳에 있는 물고기 d마리를 적은 곳으로 보냄
# 5) 인접한 칸에 대해서 동시 발생

# [4번: 일렬화]
# 1) 가장왼쪽에 있는 어항 부터 가장 아래에 있는 어항 부터
#    가장 위에있는 어항 순서대로 바닥에 일렬로 두기

# [5번: 공중 부양 작업]
# 1) 가운데를 중심으로 왼쪽 N/2개를 공중 부양시켜
#    전체를 시계 방향으로 180도 회전 시킨 다음, 오른쪽 N/2개 위에 두어야 함
# 2) 1을 한 번 더 수행
# 바닥에 있는 어항의 수는 N/4개가 된다.

# [시나리오]
# [1번: 물고기 추가]
# [2번: 어항 쌓고 돌리기]
# [3번: 물고기 수 조절]
# [4번: 일렬화]
# [5번: 공중 부양 작업]
# [6번: 물고기 수 조절]
# [7번: 일렬화]
# 물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이가
# K 이하가 되려면 어항을 몇 번 정리 ?

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def one():
    """[1번: 물고기 추가]"""

    min_cnt = min(grid[-1])

    for i in range(N):
        if grid[-1][i] == min_cnt:
            grid[-1][i] += 1


def two_1():
    # [2번: 어항 쌓고 돌리기]
    # 1) 가장 왼쪽에 있는 어항을 그 오른쪽에 있는 어항 위에 올려놓기
    grid.appendleft(deque([grid[-1].popleft()]))


def two_2():
    # [2번: 어항 쌓고 돌리기]
    # 2) 2개 이상 쌓여 있는 어항을 모두 공중 부양
    # 3) 전체를 시계방향 90도 회전
    # 4) 가장 왼쪽에 있는 어항 위에 공중 부양 시킨 어항 중 가장 왼쪽에 있는 어항 위치
    # 공중 부양시킨 어항 중 가장 오른쪽에 있는 어항의 아래에
    # 바닥에 있는 어항이 있을때까지 반복

    w_length = len(grid[0])  # 돌릴 가로 길이
    h_length = len(grid)  # 돌릴 세로 길이
    bottom_length = len(grid[-1])  # 바닥의 가로 길이

    # 돌릴 세로길이가 현재 바닥길이 - 돌릴 가로길이 보다 크다면
    if h_length > bottom_length - w_length:
        return False

    arr = deque()

    # 바닥 직전 처리
    for i in range(h_length - 1):
        arr.append(grid.popleft())

    # 바닥 처리
    temp = deque()
    for _ in range(w_length):
        temp.append(grid[-1].popleft())

    arr.append(temp)

    # 90도 회전
    arr = list(lst[::-1] for lst in list(map(list, zip(*arr))))

    for row in arr[::-1]:
        grid.appendleft(deque(row))

    return True


def three():
    """[3번: 물고기 수 조절]"""
    # 1) 모든 인접한 두 어항에 대해서 물고기 수의 차이를 구함
    # 2) 이 차이를 5로 나눈 몫을 d
    # 4) d가 0보다 크면, 두 어항 중 물고기의 수가 많은 곳에 있는 물고기 d마리를 적은 곳으로 보냄
    # 5) 인접한 칸에 대해서 동시 발생

    h_length = len(grid)  # 전체 세로 길이
    bottom_length = len(grid[-1])  # 바닥의 가로 길이

    temp_grid = [[0] * bottom_length for _ in range(h_length)]
    nxt_grid = [[0] * bottom_length for _ in range(h_length)]

    for y in range(h_length):
        for x in range(len(grid[y])):
            temp_grid[y][x] = grid[y][x]

    for y in range(h_length):
        for x in range(bottom_length):
            now_num = temp_grid[y][x]

            if now_num == 0:
                continue

            cy, cx = y, x
            num_to_change = now_num

            for k in range(4):
                ny, nx = cy + dy[k], cx + dx[k]
                if 0 <= ny < h_length and 0 <= nx < bottom_length:
                    nxt_num = temp_grid[ny][nx]
                    if nxt_num != 0:
                        d = abs(now_num - nxt_num) // 5

                        if d > 0:
                            if now_num > nxt_num:
                                num_to_change -= d
                                nxt_grid[ny][nx] += d

                            elif now_num < nxt_num:
                                num_to_change += d
                                nxt_grid[ny][nx] -= d

            nxt_grid[cy][cx] += now_num

    return nxt_grid


def four():
    """[4번: 일렬화]"""
    # 1) 가장왼쪽에 있는 어항 부터 가장 아래에 있는 어항 부터
    #    가장 위에있는 어항 순서대로 바닥에 일렬로 두기
    global grid
    lst = []
    grid = list(lst[::-1] for lst in list(map(list, zip(*grid))))

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != 0:
                lst.append(grid[y][x])

    new_grid = [lst]
    return new_grid


def five():
    """[5번: 공중 부양 작업]"""
    # 1) 가운데를 중심으로 왼쪽 N/2개를 공중 부양시켜
    #    전체를 시계 방향으로 180도 회전 시킨 다음, 오른쪽 N/2개 위에 두어야 함
    # 2) 1을 한 번 더 수행
    # 바닥에 있는 어항의 수는 N/4개가 된다.

    h_length = len(grid)  # 전체 세로 길이
    bottom_length = len(grid[-1])  # 바닥의 가로 길이

    nxt_grid = []

    for y in range(h_length):
        nxt_grid.append(grid[y][:bottom_length // 2])

    nxt_grid = list(lst[::-1] for lst in list(map(list, zip(*nxt_grid))))
    nxt_grid = list(lst[::-1] for lst in list(map(list, zip(*nxt_grid))))

    for y in range(h_length):
        nxt_grid.append(grid[y][bottom_length // 2:])

    return nxt_grid


#####################################################
N, K = map(int, input().split())
fishes = deque(map(int, input().split()))
grid = deque([fishes])
#####################################################
cnt = 0

while True:
    if max(grid[-1]) - min(grid[-1]) <= K:
        break
    # [1번: 물고기 추가]
    one()
    # [2번: 어항 쌓고 돌리기]
    two_1()

    while True:
        flag = two_2()
        if not flag:
            break
    # [3번: 물고기 수 조절]
    grid = three()
    # [4번: 일렬화]
    grid = four()
    # [5번: 공중 부양 작업]
    grid = five()
    grid = five()

    # [6번: 물고기 수 조절]
    grid = three()
    # [7번: 일렬화]
    grid = four()

    nxt_grid = deque()
    for row in grid:
        nxt_grid.append(deque(row))

    grid = nxt_grid
    cnt += 1

print(cnt)
