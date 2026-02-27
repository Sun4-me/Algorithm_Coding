from collections import deque

# # 2
# 4 1 3
# # 5
# # 6

# [1,3,6,4]
# [1,5,6,2]

# 우, 하, 좌, 상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def inb(y, x):
    return 0 <= y < N and 0 <= x < M


def rotate_dice(d):
    if d == 0:
        q1.rotate(1)
        q2[0], q2[2] = q1[0], q1[2]

    elif d == 1:
        q2.rotate(1)
        q1[0], q1[2] = q2[0], q2[2]

    elif d == 2:
        q1.rotate(-1)
        q2[0], q2[2] = q1[0], q1[2]

    elif d == 3:
        q2.rotate(-1)
        q1[0], q1[2] = q2[0], q2[2]


def bfs(y, x, B):
    v = [[0] * M for _ in range(N)]
    v[y][x] = 1
    cnt = 1
    q = deque([(y, x)])

    while q:
        cy, cx = q.popleft()

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            if inb(ny, nx):
                if grid[ny][nx] == B and v[ny][nx] == 0:
                    v[ny][nx] = 1
                    cnt += 1
                    q.append((ny, nx))

    return cnt


##########################################################
N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
##########################################################
q1 = deque([1, 3, 6, 4])
q2 = deque([1, 5, 6, 2])

cy, cx, cd = 0, 0, 0
score = 0
step = 0

while True:
    if step == K:
        break

    # 다음 이동 방향
    ny, nx = cy + dy[cd], cx + dx[cd]

    # 다음 이동 방향에 칸이 없다면
    if not inb(ny, nx):
        cd = (cd + 2) % 4
        ny, nx = cy + dy[cd], cx + dx[cd]

    cy, cx = ny, nx

    # 주사위도 돌려주기
    rotate_dice(cd)

    # A 현재 아랫면, 칸의 정수 B
    A = q1[2]
    B = grid[cy][cx]

    if A > B:
        cd = (cd + 1) % 4

    elif A < B:
        cd = (cd - 1) % 4

    # 점수 책정
    now_score = B * bfs(cy, cx, B)
    score += now_score

    step += 1

print(score)
