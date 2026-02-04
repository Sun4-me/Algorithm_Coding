def dfs(cy, cx, cnt, sm):
    global res, flag
    v[cy][cx] = 1

    if sm == 3:
        res = min(res, cnt)
        flag = True
        return

    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 상 하 좌 우
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < 5 and 0 <= nx < 5:
            if grid[ny][nx] != -1 and v[ny][nx] == 0:
                if grid[ny][nx] == 1:
                    v[ny][nx] = 1
                    grid[ny][nx] = -1
                    dfs(ny, nx, cnt + 1, sm + 1)
                    grid[ny][nx] = 1
                    v[ny][nx] = 0
                else:
                    v[ny][nx] = 1
                    grid[ny][nx] = -1
                    dfs(ny, nx, cnt + 1, sm)
                    grid[ny][nx] = 0
                    v[ny][nx] = 0


# 사과 3개를 먹기 위한 최소 이동 횟수 찾기
grid = [list(map(int, input().split())) for _ in range(5)]
s_y, s_x = map(int, input().split())

v = [[0] * 5 for _ in range(5)]

flag = False
res = 25
dfs(s_y, s_x, 0, 0)

if flag:
    print(res)
else:
    print(-1)
