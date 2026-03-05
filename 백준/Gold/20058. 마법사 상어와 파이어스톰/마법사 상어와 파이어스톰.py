from collections import deque

###################################################################
N, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2 ** N)]
command = list(map(int, input().split()))
###################################################################
def inb(y, x):
    return 0 <= y < 2 ** N and 0 <= x < 2 ** N


def bfs(y, x):
    v[y][x] = 1
    q = deque([(y, x)])

    cnt = 1

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if inb(ny, nx):
                if grid[ny][nx] > 0:
                    if v[ny][nx] == 0:
                        v[ny][nx] = 1
                        cnt += 1
                        q.append((ny, nx))

    return cnt


###################################################################
#  배열돌리기 연산 수행
flag = False

for LL in command:
    if LL != 0:
        flag = True

        for L in range(1, LL + 1):

            window = 2 ** L  # 쪼개는 범위
            w = 2 ** (L - 1)  # 부분 격자 범위

            new_grid = [[] for _ in range(2 ** N)]

            for y in range(0, 2 ** N, window):
                now_arr_y = grid[y:y + window]

                # 격자 쪼개기
                for x in range(0, 2 ** N, window):
                    now_grid = []

                    for row in now_arr_y:
                        now_grid.append(row[x: x + window])

                    # 부분 격자 돌리기
                    for i in range(w, window):
                        new_grid[y + i - w].extend(now_grid[i][:w])
                        new_grid[y + i].extend(now_grid[i][w:])

                    # 부분 격자 돌리기
                    for i in range(w):
                        new_grid[y + i + w].extend(now_grid[i][w:])
                        new_grid[y + i].extend(now_grid[i][:w])

            grid = new_grid

    if not flag:
        new_grid = grid

    # 3개의 얼음과 인접해 있지 않은 칸은 양을 1 빼기
    to_change = []

    for y in range(2 ** N):
        for x in range(2 ** N):
            if new_grid[y][x] == 0:
                continue

            cnt = 0

            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ny, nx = y + dy, x + dx
                if inb(ny, nx):
                    if new_grid[ny][nx] > 0:
                        cnt += 1

            if cnt < 3:
                to_change.append((y, x))

    for y, x in to_change:
        new_grid[y][x] -= 1

    grid = new_grid
###################################################################
v = [[0] * (2 ** N) for _ in range(2 ** N)]
ans = 0
for y in range(2 ** N):
    for x in range(2 ** N):
        if grid[y][x] >= 1:
            if v[y][x] == 0:
                now_sum = bfs(y, x)
                ans = max(ans, now_sum)

print(sum(sum(row) for row in grid))
print(ans)
