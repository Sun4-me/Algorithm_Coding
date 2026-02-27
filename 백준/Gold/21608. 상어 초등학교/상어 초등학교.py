# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def inb(y, x):
    return 0 <= y < N and 0 <= x < N


def count_fav_space(y, x, k):
    """현재 좌표의 사방 좋아하는 사람 리턴"""
    now_fav = set(k)

    spcae_cnt = 0
    fav_cnt = 0

    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if inb(ny, nx):
            if grid[ny][nx] in now_fav:
                fav_cnt += 1

            elif grid[ny][nx] == 0:
                spcae_cnt += 1

    return fav_cnt, spcae_cnt


################################################
N = int(input())
student = dict()
order = []
for _ in range(N ** 2):
    lines = list(map(int, input().split()))
    now_num = lines[0]
    favorite = lines[1:]

    order.append(now_num)
    student[now_num] = favorite

grid = [[0] * N for _ in range(N)]
################################################
# 자리 배치 하기

for now_s in order:
    now_fav = student[now_s]

    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸
    possible = []

    for y in range(N):
        for x in range(N):
            if grid[y][x] == 0:
                fav_cnt, spa_cnt = count_fav_space(y, x, now_fav)
                possible.append((fav_cnt, spa_cnt, y, x))

    possible.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))

    # 자리 배치.
    cy, cx = possible[0][2], possible[0][3]
    grid[cy][cx] = now_s

###########################
ans = 0

# 만족도 구하기
for y in range(N):
    for x in range(N):
        now_s = grid[y][x]
        now_fav = set(student[now_s])
        fav_cnt = 0

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if inb(ny, nx):
                if grid[ny][nx] in now_fav:
                    fav_cnt += 1

        if fav_cnt == 0:
            continue
        elif fav_cnt == 1:
            ans += 1
        elif fav_cnt == 2:
            ans += 10
        elif fav_cnt == 3:
            ans += 100
        elif fav_cnt == 4:
            ans += 1000

###########################
print(ans)
