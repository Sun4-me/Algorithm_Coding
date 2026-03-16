# [초기 정보]
# N x N 격자
# 상어: 1 ~ M 자연수 번호
# 1번 상어는 강력하다 !

# [시나리오]
# 1) 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
# 2) 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동,
#    자신의 냄새를 그 칸에 뿌린다. 냄새는 k번 이동하고 나면 사라진다.
# 3) 모든 상어가 이동 한 후 한 칸에 여러 마리 상어가 남아 있으면,
#    가장 작은 번호를 가진 상어를 제외하고 죽여버리기


# [상어의 이동 방향 결정]
# 1) 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
# 2) 그러한 칸이 없다면 자신의 냄새가 있는 칸의 방향으로 잡는다.
# 3) 이때 가능한 칸이 여러개이면 특수 우선순위를 따른다.

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def inb(y, x):
    return 0 <= y < N and 0 <= x < N


def smelling():
    """모든 상어가 현재 위치에 번호와 K를 남겨둠"""
    for y in range(N):
        for x in range(N):
            if shark_grid[y][x]:
                if smell_grid:
                    smell_grid[y][x].clear()
                num = shark_grid[y][x][0][0]
                smell_grid[y][x].extend([num, K])


def time_go_k_down():
    """시간이 지나서 k 감소 시키기"""
    for y in range(N):
        for x in range(N):
            if smell_grid[y][x]:
                if smell_grid[y][x][1] == 1:
                    smell_grid[y][x].clear()
                else:
                    smell_grid[y][x][1] -= 1


def shark_move():
    """상어의 이동, 이동 하면서 겹치는것도 처리"""
    only_one = False
    cnt = 0

    nxt_shark_grid = [[[] for _ in range(N)] for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if shark_grid[y][x]:
                cnt += 1

                num, cd = shark_grid[y][x][0]
                ny, nx, nd = where_to_go(num, y, x, cd)

                if not nxt_shark_grid[ny][nx]:
                    nxt_shark_grid[ny][nx].append([num, nd])

                else:
                    taget_num = nxt_shark_grid[ny][nx][0][0]
                    # 안에 있는게 더 작다면
                    if taget_num < num:
                        continue

                    else:
                        nxt_shark_grid[ny][nx].clear()
                        nxt_shark_grid[ny][nx].append([num, nd])

    if cnt == 1:
        only_one = True

    return nxt_shark_grid, only_one


# [상어의 이동 방향 결정]
# 1) 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
# 2) 그러한 칸이 없다면 자신의 냄새가 있는 칸의 방향으로 잡는다.
# 3) 이때 가능한 칸이 여러개이면 특수 우선순위를 따른다.
def where_to_go(num, cy, cx, cd):
    """상어의 이동 방향 결정"""

    # 인접한 칸 중 아무 냄새가 없는 칸.
    # 현재 상어의 현재 방향 기준 특수 우선 순위 적용

    for k in direct[num][cd]:
        ny, nx = cy + dy[k], cx + dx[k]
        if not inb(ny, nx):
            continue

        if smell_grid[ny][nx]:
            continue

        if not shark_grid[ny][nx]:
            return ny, nx, k

    # 빈칸으로 이동 못했다면 자신의 냄새가 있는 칸이라도 가야함
    for k in direct[num][cd]:
        ny, nx = cy + dy[k], cx + dx[k]
        if not inb(ny, nx):
            continue

        if smell_grid[ny][nx][0] == num:
            return ny, nx, k


##########################################################
N, M, K = map(int, input().split())

temp = [list(map(int, input().split())) for _ in range(N)]
start_direct = [0] + list(map(int, input().split()))

direct = [[[] for _ in range(4)] for _ in range(M + 1)]

step = 0
for num in range(4 * M):
    num = num // 4 + 1
    A, B, C, D = map(int, input().split())
    direct[num][step].extend([A - 1, B - 1, C - 1, D - 1])
    step = (step + 1) % 4

shark_grid = [[[] for _ in range(N)] for _ in range(N)]
smell_grid = [[[] for _ in range(N)] for _ in range(N)]

# [상어번호, 방향]
for y in range(N):
    for x in range(N):
        if temp[y][x] != 0:
            num = temp[y][x]
            dir = start_direct[num] - 1
            shark_grid[y][x].append([num, dir])
##########################################################
# [시나리오]
# 1) 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
# 2) 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동,
#    자신의 냄새를 그 칸에 뿌린다. 냄새는 k번 이동하고 나면 사라진다.
# 3) 모든 상어가 이동 한 후 한 칸에 여러 마리 상어가 남아 있으면,
#    가장 작은 번호를 가진 상어를 제외하고 죽여버리기

ans = 0
smelling()

while True:
    if ans == 1001:
        ans = -1
        break

    # 상어 이동
    shark_grid, only_one = shark_move()

    if only_one:
        break

    # 냄새 감소
    time_go_k_down()

    # 냄새 뿌리기
    smelling()

    ans += 1

print(ans)

# print("상어 그리드")
# for row in shark_grid:
#     print(*row)
# print()
#
# print("냄새 그리드")
# for row in smell_grid:
#     print(*row)
