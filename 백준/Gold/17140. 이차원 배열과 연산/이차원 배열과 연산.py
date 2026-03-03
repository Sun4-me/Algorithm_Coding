# [정렬 방법]
# 수의 등장 횟수 오름차순
# 수 오름차순
# [수, 등장횟수]
from collections import defaultdict


def one_row_cal(y):
    global w

    new_arr = []
    # key: 수, value: 등장횟수
    d = defaultdict(int)

    for x in range(w):
        d[grid[y][x]] += 1

    row = [(key, value) for key, value in d.items() if key != 0]
    row.sort(key=lambda x: (x[1], x[0]))

    for i in range(len(row)):
        new_arr.append(row[i][0])
        new_arr.append(row[i][1])

    return new_arr


def row_cal():
    global w
    new_grid = []

    # r연산 진행
    for y in range(h):
        new_grid.append(one_row_cal(y))

    # w값 갱신
    for y in range(h):
        w = max(w, len(new_grid[y]))

    if w > 100:
        w = 100

    # 0 채우기
    for y in range(h):
        row_length = len(new_grid[y])

        if row_length < w:
            for _ in range(w - row_length):
                new_grid[y].append(0)

    return new_grid


##############################################################
R, C, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(3)]
##############################################################
# 행의 개수, 열의 개수
h, w = 3, 3

time = 0

while True:
    if 0 <= R - 1 < h and 0 <= C - 1 < w:
        if grid[R - 1][C - 1] == K:
            break

    if time == 101:
        break

    # r연산
    if h >= w:
        new_grid = row_cal()

    # c연산
    elif h < w:
        # 전치
        grid = [lst for lst in list(map(list, zip(*grid)))]
        h, w = w, h

        new_grid = row_cal()

        # 다시 돌려줌
        new_grid = [lst for lst in list(map(list, zip(*new_grid)))]
        h, w = w, h

    if w > 100:
        w = 100

    if h > 100:
        h = 100

    grid = new_grid
    time += 1

if time == 101:
    print(-1)

else:
    print(time)
