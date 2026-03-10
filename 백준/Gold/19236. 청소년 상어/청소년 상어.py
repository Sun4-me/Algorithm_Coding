# [물고기의 이동]
# 1<=번호<=16, 8방향
# 번호가 작은 물고기부터 이동
# 한 칸 이동. 빈칸 or 다른 물고기가 있는 칸만 가능
# 이동하는 곳에 물고기가 있다면 위치 교환
# 현재 방향으로 갈 수 없다면 이동할 수 있는 칸을 향할때까지 방향 45회전
# 이동 못하면 제자리

# [상어의 이동]
# (0, 0) 에 있는거 먹고 방향 흡수하고 시작
# 여러개 칸 이동 가능
# 물고기가 있는 칸만 이동 가능 ????????? ㅋㅋㅋㅋ하 ㅋㅋㅋㅋ하 ㅋㅋㅋㅋ하 ㅋㅋㅋㅋ하 ㅋㅋㅋㅋ하 ㅋㅋㅋㅋ하 ㅋㅋㅋㅋ하 ㅋㅋㅋㅋ하 ㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜ
# 이동할 수 있는 칸이 없으면 종료

# [전체 시나리오]
# 1. 상어의 이동
# 2. 물고기의 이동
# 3. 상어 더 이상 못 움직이면 먹은 번호의 합 리턴
# 4. 최대값 찾기
# 상, 상좌, 좌, 하좌, 하, 하우, 우, 상우

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


def inb(y, x):
    return 0 <= y < 4 and 0 <= x < 4


def fishes_move(grid, fishes, shark):
    for i in range(1, 17):

        if fishes[i] == 0:
            continue

        cy, cx, cd = fishes[i]
        c_num = i
        k = cd
        step = 0

        while True:
            if step == 8:
                break

            ny, nx = cy + dy[k], cx + dx[k]
            # 격자 안이며
            if inb(ny, nx):
                # 상어가 있는 곳이 아닌 경우
                if (ny, nx) != (shark[0], shark[1]):
                    # 빈칸인 경우
                    if grid[ny][nx] == 0:
                        grid[ny][nx] = c_num
                        grid[cy][cx] = 0
                        fishes[c_num] = (ny, nx, k)
                        break

                    # 물고기가 있는 경우
                    else:
                        target_num = grid[ny][nx]
                        _, _, td = fishes[target_num]

                        fishes[c_num], fishes[target_num] = (ny, nx, k), (cy, cx, td)
                        grid[ny][nx], grid[cy][cx] = c_num, target_num
                        break

            step += 1
            k = (k + 1) % 8


def shark_can_move(grid, shark):
    flag = False
    possible = []
    cy, cx, cd = shark

    while True:
        ny, nx = cy + dy[cd], cx + dx[cd]
        if inb(ny, nx):
            if grid[ny][nx] != 0:
                flag = True
                possible.append((ny, nx, cd))
                cy, cx = ny, nx

            else:
                cy, cx = ny, nx

        else:
            break

    return possible, flag


def back(grid, fishes, shark, sm):
    global ans
    nxt_fishes = fishes[:]
    nxt_grid = [lst[:] for lst in grid]

    fishes_move(nxt_grid, nxt_fishes, shark)
    lst, flag = shark_can_move(nxt_grid, shark)

    if not flag:
        ans = max(ans, sm)
        return

    for ny, nx, _, in lst:
        target_num = nxt_grid[ny][nx]
        ty, tx, td = nxt_fishes[target_num]

        nxt_grid[ny][nx] = 0
        nxt_fishes[target_num] = 0
        nxt_shark = ny, nx, td

        back(nxt_grid, nxt_fishes, nxt_shark, sm + target_num)

        nxt_grid[ny][nx] = target_num
        nxt_fishes[target_num] = (ty, tx, td)


############################################################
ori_fishes = [0] * 17

for y in range(4):
    lines = list(map(int, input().split()))
    for x in range(4):
        num, direct = lines[x * 2], lines[x * 2 + 1]
        ori_fishes[num] = (y, x, direct - 1)
############################################################
# 초기값
ori_grid = [[0] * 4 for _ in range(4)]
ans = 0

for i in range(1, 17):
    y, x, d = ori_fishes[i]
    ori_grid[y][x] = i

first_num = ori_grid[0][0]
_, _, sd = ori_fishes[first_num]
ori_fishes[first_num] = 0
ori_shark = (0, 0, sd)
ori_grid[0][0] = 0

ans += first_num
############################################################
back(ori_grid, ori_fishes, ori_shark, first_num)
print(ans)
