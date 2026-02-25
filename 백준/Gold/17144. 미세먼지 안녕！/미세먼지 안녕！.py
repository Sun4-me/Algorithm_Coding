# 공기청정기는 항상 1번 열에 설치, 크기는 두 행을 차지
# 공기청정기가 설치되어 있지 않은 칸에는 미세먼지. 칸에 있는 양 만큼.A

# 1초 동안 발생하는 일
# 1. 미세먼지가 있는 모든 칸에서 확산이 일어남
# - 인접한 네 방향
# - 공기청정기가 있거나 칸이 없으면 확산 x
# - 확산되는 양은 A / 5 소수점은 버린다.
# - A에서 남아있는 미세먼지는 A - (A/5 * 확산된 방향의 개수)

# 2. 공기 청정기의 작동
# - 위쪽 공청기는 반시계 아래쪽 공청기는 시계 방향
# - 바람의 방향대로 한칸씩 이동
# - 공청기로 들어가면 미세먼지는 사라짐

def inb(y, x):
    return 0 <= y < N and 0 <= x < M


def fly_dust(y, x):
    """미세먼지 있는 칸에서 확산, 확산 후 남은 값도 저장"""

    now_dust = grid[y][x]

    if now_dust < 5:
        tmp_grid[y][x] += now_dust
        return

    # 뿌릴 먼지의 양
    go_dust = grid[y][x] // 5

    # 확산 방향 카운트
    cnt = 0

    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = y + dy, x + dx
        if inb(ny, nx):
            if (ny, nx) not in (up_cleaner, down_cleaner):
                tmp_grid[ny][nx] += go_dust
                cnt += 1

    # 남은 양 현재칸에 저장
    tmp_grid[y][x] += now_dust - (go_dust * cnt)


def up_work():
    """위쪽  공기 청정기 작동 | 반시계 방향"""
    cy, cx = up_cleaner

    # 우 상 좌 하
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]

    y, x = cy, 1  # 공기청정기 바로 오른쪽 칸부터 시작
    prev_val = 0  # 공기청정기에서 나오는 깨끗한 공기

    for k in range(4):
        while True:
            ny, nx = y + dy[k], x + dx[k]

            # 위쪽 공기청정기 영역 제한 (0 <= ny <= cy)
            if not (0 <= ny <= cy and 0 <= nx < M):
                break

            # 공기청정기로 돌아왔을 때, 마지막 칸(현재 y, x)을 업데이트하고 종료
            if (ny, nx) == (cy, cx):
                tmp_grid[y][x], prev_val = prev_val, tmp_grid[y][x]
                break

            tmp_grid[y][x], prev_val = prev_val, tmp_grid[y][x]
            y, x = ny, nx


def down_work():
    """ 아래쪽 공기 청정기 작동 | 시계 방향"""
    cy, cx = down_cleaner

    # 우 하 좌 상
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    y, x = cy, 1  # 공기청정기 바로 오른쪽 칸부터 시작
    prev_val = 0  # 공기청정기에서 나오는 깨끗한 공기

    for k in range(4):
        while True:
            ny, nx = y + dy[k], x + dx[k]

            # 아래쪽 공기청정기 영역 제한 (cy <= ny < N)
            if not (cy <= ny < N and 0 <= nx < M):
                break

            # 공기청정기로 돌아왔을 때, 마지막 칸(현재 y, x)을 업데이트하고 종료
            if (ny, nx) == (cy, cx):
                tmp_grid[y][x], prev_val = prev_val, tmp_grid[y][x]
                break

            tmp_grid[y][x], prev_val = prev_val, tmp_grid[y][x]
            y, x = ny, nx


###########################################################
N, M, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
###########################################################
up_cleaner = (0, 0)
down_cleaner = (0, 0)
dusts = set()
###########################################################
# 공청기 위치 찾기
# 처음꺼는 위, break. 아래는 y+1
for y in range(N):
    if grid[y][0] == -1:
        up_cleaner = (y, 0)
        down_cleaner = (y + 1, 0)
        break
###########################################################
# T초 만큼 돌리기
while T:
    tmp_grid = [[0] * M for _ in range(N)]

    T -= 1

    for y in range(N):
        for x in range(M):
            if grid[y][x] > 0:
                fly_dust(y, x)

    up_work()
    down_work()

    grid = [row[:] for row in tmp_grid]
###########################################################
ans = 0
for y in range(N):
    for x in range(M):
        if grid[y][x] > 0:
            ans += grid[y][x]

print(ans)
