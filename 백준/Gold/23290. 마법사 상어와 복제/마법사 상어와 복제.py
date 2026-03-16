## 상어의 마법 연습 한 번
# [1]. 복제 마법 시전
# 단계 [5] 번에서 현재의 물고기가 복제되어 칸에 나타난다.

# [2]. 물고기의 이동
# 모든 물고기가 한 칸 이동 한다.
# 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동 불가
# 각 물고기가 가지고 있는 이동방향 기준 갈 수 있을때까지 45반시계 회전
# 이동 할 수 있는 칸이 없으면 이동 X

# [3]. 상어의 이동
# 상어가 연속해서 3칸 이동한다.
# 상하좌우 인접한 칸으로 이동 가능
# 격자를 벗어나면 안된다.
# 연속해서 이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면,
# 그 칸에 있는 모든 물고기는 격자에서 제외,
# 제외되는 모든 물고기는 물고기 냄새를 남긴다.
# 가능한 이동 방법 중에서 제외되는 물고기의 수 가 가장 많은 방법으로 이동
# 그러한 방법이 여러가지인 경우 사전순으로 가장 앞서는 방법을 이용 할 것

# [4]. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.

# [5]. [1]에서 사용한 복제 마법이 완료, 1에서의 위치와 방향을 그대로 복제됨
from itertools import product

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상 좌 하 우
ddy = [-1, 0, 1, 0]
ddx = [0, -1, 0, 1]


def fish_move():
    nxt_grid = [[[] for _ in range(4)] for _ in range(4)]

    for y in range(4):
        for x in range(4):
            for d in grid[y][x]:
                cy, cx, cd = y, x, d
                step = 0
                while True:
                    if step == 8:
                        nxt_grid[cy][cx].append(d)
                        break

                    step += 1

                    ny, nx = cy + dy[cd], cx + dx[cd]

                    # 1) 격자 밖
                    if not (0 <= ny < 4 and 0 <= nx < 4):
                        cd = (cd - 1) % 8
                        continue

                    # 2) 상어 위치
                    if (ny, nx) == (shark_y, shark_x):
                        cd = (cd - 1) % 8
                        continue

                    # 3) 냄새 나는 곳
                    if v[ny][nx]:
                        cd = (cd - 1) % 8
                        continue

                    # 이동
                    nxt_grid[ny][nx].append(cd)
                    break

    return nxt_grid


def shark_move():
    global shark_y, shark_x

    eat_fishes = []

    for direct in case:
        cy, cx = shark_y, shark_x
        cnt = 0
        v_shark = [[False] * 4 for _ in range(4)]

        for k in direct:
            cy, cx = cy + ddy[k - 1], cx + ddx[k - 1]

            if not (0 <= cy < 4 and 0 <= cx < 4):
                cnt = -1
                break

            if grid[cy][cx] and not v_shark[cy][cx]:
                v_shark[cy][cx] = True
                cnt += len(grid[cy][cx])

        eat_fishes.append(cnt)

    max_cnt = max(eat_fishes)
    max_idx = -1

    for i in range(64):
        if eat_fishes[i] == max_cnt:
            max_idx = i
            break

    cy, cx = shark_y, shark_x
    for k in case[max_idx]:
        cy, cx = cy + ddy[k - 1], cx + ddx[k - 1]
        if grid[cy][cx]:
            grid[cy][cx].clear()
            v[cy][cx] = 2

        shark_y, shark_x = cy, cx


##############################################################
# M: 물고기의 수, S: 연습 횟 수
M, S = map(int, input().split())
grid = [[[] for _ in range(4)] for _ in range(4)]

for _ in range(M):
    y, x, d = map(int, input().split())
    grid[y - 1][x - 1].append(d - 1)

shark_y, shark_x = map(int, input().split())
shark_y -= 1
shark_x -= 1

v = [[0] * 4 for _ in range(4)]
##############################################################
case = []  # 상어 이동 방법 들
for p in product(range(1, 5), repeat=3):
    case.append(p)

for i in range(S):
    # [1]. 복제 마법 시전
    copy_grid = [lst[:] for lst in grid[:]]

    # [2]. 물고기의 이동
    grid = fish_move()

    # [4]. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
    for y in range(4):
        for x in range(4):
            if v[y][x] != 0:
                v[y][x] -= 1

    # [3]. 상어의 이동
    shark_move()

    # [5]. [1]에서 사용한 복제 마법이 완료, 1에서의 위치와 방향을 그대로 복제됨
    for y in range(4):
        for x in range(4):
            if copy_grid[y][x]:
                grid[y][x].extend(copy_grid[y][x])
##############################################################
ans = 0
for y in range(4):
    for x in range(4):
        ans += len(grid[y][x])

print(ans)
