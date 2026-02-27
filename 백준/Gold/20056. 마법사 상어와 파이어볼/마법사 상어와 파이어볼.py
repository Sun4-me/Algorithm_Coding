# 상 상우 우 하우 하 하좌 좌 상좌
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
grid = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    R, C, M, S, D = map(int, input().split())
    grid[R - 1][C - 1].append([M, S, D])
###############################################################
time = 0
while True:
    if time == K:
        break

    next_grid = [[[] for _ in range(N)] for _ in range(N)]
    v = [[0] * N for _ in range(N)]

    # 모든 파이어볼의 이동
    for y in range(N):
        for x in range(N):
            for fire_ball in grid[y][x]:
                m, s, d = fire_ball
                ny, nx = (y + (dy[d] * s)) % N, (x + (dx[d] * s)) % N

                next_grid[ny][nx].append([m, s, d])
                v[ny][nx] += 1

    # 이동이 끝난 뒤 2개 이상의 파이어볼이 있는 칸
    for y in range(N):
        for x in range(N):
            if v[y][x] >= 2:
                tot_m, tot_s, tot_cnt = 0, 0, 0
                tot_d = []

                for fire_ball in next_grid[y][x]:
                    m, s, d = fire_ball
                    tot_cnt += 1
                    tot_m += m
                    tot_s += s
                    tot_d.append(d)

                next_grid[y][x] = []

                next_m = tot_m // 5

                if next_m == 0:
                    continue

                next_s = tot_s // tot_cnt
                flag = True  # 모두 홀수이거나 모두 짝수

                if tot_d[0] % 2 == 0:
                    for i in tot_d:
                        if i % 2 != 0:
                            flag = False
                            break

                elif tot_d[0] % 2 == 1:
                    for i in tot_d:
                        if i % 2 != 1:
                            flag = False
                            break

                if flag:
                    next_grid[y][x].append([next_m, next_s, 0])
                    next_grid[y][x].append([next_m, next_s, 2])
                    next_grid[y][x].append([next_m, next_s, 4])
                    next_grid[y][x].append([next_m, next_s, 6])

                else:
                    next_grid[y][x].append([next_m, next_s, 1])
                    next_grid[y][x].append([next_m, next_s, 3])
                    next_grid[y][x].append([next_m, next_s, 5])
                    next_grid[y][x].append([next_m, next_s, 7])

    grid = next_grid
    time += 1

ans = 0
for y in range(N):
    for x in range(N):
        if v[y][x] > 0:
            for fire_ball in grid[y][x]:
                ans += fire_ball[0]

print(ans)
