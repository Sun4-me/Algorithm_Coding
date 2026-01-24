# 10×10
# 구사과와 큐브러버
# 구사과 먼저
# 구사과가 한번 더 가졌을때 이길 수 있을까

grid = [list(map(str, input())) for _ in range(10)]
search = (-1, -1), (0, -1), (+1, -1), (-1, 0), (+1, 0), (-1, +1), (0, +1), (+1, +1)
offset = 0

can_win = 0

for cy in range(10):
    for cx in range(10):
        if grid[cy][cx] == "X":
            for dx, dy in search:
                tmp = []
                curr_x, curr_y = cx, cy
                tmp.append(grid[cy][cx])
                for _ in range(4):
                    nx, ny = curr_x + dx, curr_y + dy

                    # 범위 체크
                    if nx < 0 or nx > 9 or ny < 0 or ny > 9:
                        break

                    # 돌 확인
                    if grid[ny][nx] == "O":
                        break

                    if grid[ny][nx] == "X" or grid[ny][nx] == ".":
                        tmp.append(grid[ny][nx])
                        # 계속 나아기 위한 좌표 갱신
                        curr_x, curr_y = nx, ny

                    else:
                        break

                if len(tmp) == 5 and tmp.count("X") == 4:
                    can_win = 1
print(can_win)
