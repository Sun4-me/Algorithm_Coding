# 검은 바둑알 1, 흰 바둑알 2
# 코드 리셋 새로운 마음으로 다시 시작
grid = [list(map(int, input().split())) for _ in range(19)]

# 우 하 우하 우상 (좌표 출력 기준에 맞춰서)
dy = [0, 1, 1, -1]
dx = [1, 0, 1, 1]

for y in range(19):
    for x in range(19):
        if grid[y][x] != 0:
            dol_color = grid[y][x]

            for k in range(4):
                cnt = 1
                ny = y + dy[k]
                nx = x + dx[k]

                while 0 <= ny < 19 and 0 <= nx < 19 and grid[ny][nx] == dol_color:
                    cnt += 1
                    ny += dy[k]
                    nx += dx[k]

                # 5개라면
                if cnt == 5:
                    prev_y = y - dy[k]
                    prev_x = x - dx[k]

                    # 지금이 시작점인지 확인
                    if 0 <= prev_y < 19 and 0 <= prev_x < 19 and grid[prev_y][prev_x] == dol_color:
                        continue

                    print(dol_color)
                    print(y + 1, x + 1)
                    quit()

# 승부가 안난 경우
print(0)
