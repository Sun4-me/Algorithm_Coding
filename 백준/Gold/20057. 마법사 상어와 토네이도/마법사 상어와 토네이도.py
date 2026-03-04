# 좌 하 우 상
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


def inb(y, x):
    return 0 <= y < N and 0 <= x < N


def cleaning(y, x, d):
    global ans
    total_dust = grid[y][x]
    sum_go_dust = 0

    # 0이면 더 볼 필요 없음
    if total_dust == 0:
        return

    grid[y][x] = 0  # 이 부분은 청소 완료 할테니까

    for ddy, ddx, percent in patterns[d]:
        ny, nx = y + ddy, x + ddx

        if percent == 0:  # a 위치인 경우, 마지막으로 들어옴
            go_dust = total_dust - sum_go_dust

        else:
            go_dust = (total_dust * percent) // 100
            sum_go_dust += go_dust

        # 범위 밖이면
        if not inb(ny, nx):
            ans += go_dust

        else:
            grid[ny][nx] += go_dust


##################################################
# 패턴 저장 (dy, dx, percent)
left_pattern = [
    (-2, 0, 2), (2, 0, 2),
    (-1, -1, 10), (1, -1, 10),
    (-1, 0, 7), (1, 0, 7),
    (-1, 1, 1), (1, 1, 1),
    (0, -2, 5),
    (0, -1, 0)  # a% 위치
]

patterns = [left_pattern]

for _ in range(3):
    prev = patterns[-1]
    # 이전 것 반시계 방향 돌리기
    nxt = [(-x, y, percent) for y, x, percent in prev]
    patterns.append(nxt)
##################################################
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
##################################################
cy, cx = N // 2, N // 2
step = 0  # 2번 움직일때마다 회전용
w = 1  # 얼만큼 움직일지
d = 0  # 왼쪽 방향

ans = 0  # 밖으로 나간 먼지

flag = True # (0, 0) 까지

while flag:

    if step == 2:
        step = 0
        w += 1

    for _ in range(w):
        cy, cx = cy + dy[d], cx + dx[d]

        if (cy, cx) == (0, -1):
            flag = False
            break

        cleaning(cy, cx, d)

    step += 1
    d = (d + 1) % 4

print(ans)
