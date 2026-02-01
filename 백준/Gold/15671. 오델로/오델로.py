###########################################################

# 현재 칼러로 8방향으로 검사
# 검사하면서 저장한 반대 칼러의 인덱스들에 대해 현재 칼러로 뒤집고 현재 위치에 돌두기

def play(y, x, color):
    target_idx = []
    for k in range(8):
        tmp_idx = []
        flag = False
        cy, cx = y, x
        while True:
            ny, nx = cy + dy[k], cx + dx[k]
            if 0 <= ny < 6 and 0 <= nx < 6:
                # 반대 색상 마주침. 뒤집을 가능성이 있으니 리스트에 넣어둠
                if grid[ny][nx] == -color:
                    tmp_idx.append((ny, nx))
                    cy, cx = ny, nx
                    # 뒤집을 수 있다
                    flag = True
                # 포위하고 있다면
                elif flag and grid[ny][nx] == color:
                    target_idx += tmp_idx
                    break
                else:
                    break
            else:
                break
    # 뒤집고 돌 두기
    grid[y][x] = color
    for y, x in target_idx:
        grid[y][x] = color


###########################################################
n = int(input())
logs = [list(map(int, input().split())) for _ in range(n)]
grid = [[0] * 6 for _ in range(6)]
###########################################################
# -1: W, 1: B
grid[2][2] = -1
grid[3][3] = -1
grid[2][3] = 1
grid[3][2] = 1
###########################################################
# 상 하 좌 우 대상좌 대상우 대하좌 대하우
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
###########################################################
# -1: W, 1: B
color = 1
for log in logs:
    cy, cx = log[0] - 1, log[1] - 1
    play(cy, cx, color)
    color *= -1  # 턴넘기기
###########################################################
# 결과 출력
w_count = 0
b_count = 0
for row in range(6):
    for col in range(6):
        if grid[row][col] == -1:
            grid[row][col] = "W"
            w_count += 1
        elif grid[row][col] == 1:
            grid[row][col] = "B"
            b_count += 1
        else:
            grid[row][col] = "."

for row in grid:
    print(*row, sep="")

if w_count > b_count:
    print("White")
else:  # 비기는 경우는 안 준다고 함
    print("Black")
