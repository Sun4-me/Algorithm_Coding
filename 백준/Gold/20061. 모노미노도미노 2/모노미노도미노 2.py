# [블록의 정의]
# 타일 하나 또는 두개가 | 가로 또는 세로로 붙어 있는 형태

# [블록의 이동]
# 1) 빨간색 보드에서 놓을 위치를 선택
# 2) 초록색 보드로 이동, 파란색 보드로 이동
# 3) 다른 블록을 만나거나 보드의 경계를 만나기전까지 계속해서 이동

## [이동 후 규칙]
# [행과 열 가득참 규칙]
# 초록색 보드의 특정행이 가득차 있다면 그 행의 타일은 모두 사라진다.
# 사라진 이후에는 사라진 행 위에 있는 블록이 사라진 행의 수 만큼 아래로 이동
# 파란색의 경우 열이 가득차있으면 열의 타일이 모두 사라지며
# 사라진 이후에는 사라진 열의 왼쪽에 있는 블록이 사라진 열의 수만큼 오른쪽으로 이동
####### 한행이나 한열이나 사라지면 점수 +1
# [특별한 칸 규칙]
# 반드시 [행과 열 가득참 규칙]을 모두 수행 후, [특별한 칸 규칙]을 수행할 것
# 연한 칸에 블록이 위치해 있으면 블록이 있는 행/열의 수만큼 아래 행/오른쪽 열 에 타일이 사라짐
# 사라진 수 만큼 모든 블록이 아래/오른쪽으로 이동

# 0: 하, 1: 우
dy = [1, 0]
dx = [0, 1]


def inb(y, x):
    return 0 <= y < 10 and 0 <= x < 10


def check_move(ny, nx):
    if not inb(ny, nx):
        return False
    if grid[ny][nx] != 0:
        return False

    return True


def first_move(lst, k):
    """빨간 보드에서의 이동
    k == 0 초록색으로
    k == 1 파란색으로  """

    move_flag = True

    while move_flag:

        for cy, cx in lst:
            ny, nx = cy + dy[k], cx + dx[k]
            if not check_move(ny, nx):
                move_flag = False
                break

        if move_flag:
            for i in range(len(lst)):
                cy, cx = lst[i]
                ny, nx = cy + dy[k], cx + dx[k]
                lst[i] = (ny, nx)

    for y, x in lst:
        grid[y][x] = 1


def full():
    """
    초록색보드, 파란색모두 행/열 처리, 점수 계산
    """
    global score

    # 초록색 보드 조치
    while True:

        for y in range(9, 3, -1):
            # 모든 행이 1이라면
            if all(grid[y]):
                score += 1

                # 행 지우기
                for x in range(4):
                    grid[y][x] = 0

                # 행 위에 있는 모든 타일을 한칸씩 아래로 이동하기
                for ty in range(y - 1, 3, -1):
                    for x in range(4):
                        if grid[ty][x] == 1:
                            grid[ty][x] = 0
                            grid[ty + 1][x] = 1
                break
        else:
            break

    # 파란색 보드 조치
    while True:

        for x in range(9, 3, -1):

            for y in range(4):
                if grid[y][x] == 0:
                    break

            # 한 열이 다 1이라면
            else:
                score += 1

                # 열 지우기
                for y in range(4):
                    grid[y][x] = 0

                # 열 왼쪽에 있는 모든 타일을 한 칸씩 오른쪽으로 옮기기
                for tx in range(x - 1, 3, -1):
                    for y in range(4):
                        if grid[y][tx] == 1:
                            grid[y][tx] = 0
                            grid[y][tx + 1] = 1

                break

        else:
            break


# [특별한 칸 규칙]
# 반드시 [행과 열 가득참 규칙]을 모두 수행 후, [특별한 칸 규칙]을 수행할 것
# 연한 칸에 블록이 위치해 있으면 블록이 있는 행/열의 수만큼 아래 행/오른쪽 열 에 타일이 사라짐
# 사라진 수 만큼 모든 블록이 아래/오른쪽으로 이동
def special_rule():
    # 초록색 보드 조치
    cnt_green = 0  # 블록이 있는 행의 수

    for x in range(4):
        if grid[4][x] == 1:
            cnt_green += 1
            break

    for x in range(4):
        if grid[5][x] == 1:
            cnt_green += 1
            break

    while cnt_green:
        cnt_green -= 1

        # 맨 아래행 비우기
        for x in range(4):
            grid[9][x] = 0

        # 이동 시키기
        for y in range(8, 3, -1):
            for x in range(4):
                if grid[y][x] == 1:
                    grid[y][x] = 0
                    grid[y + 1][x] = 1

    # 파란색 보드 조치
    cnt_blue = 0  # 블록이 있는 열의 수

    for y in range(4):
        if grid[y][4] == 1:
            cnt_blue += 1
            break

    for y in range(4):
        if grid[y][5] == 1:
            cnt_blue += 1
            break

    while cnt_blue:
        cnt_blue -= 1

        # 맨 오른쪽 열 비우기
        for y in range(4):
            grid[y][9] = 0

        # 이동 시키기
        for x in range(8, 3, -1):
            for y in range(4):
                if grid[y][x] == 1:
                    grid[y][x] = 0
                    grid[y][x + 1] = 1


def make_coord(t, y, x):
    lst = []
    if t == 1:
        lst.append((y, x))
    elif t == 2:
        lst.append((y, x))
        lst.append((y, x + 1))

    elif t == 3:
        lst.append((y, x))
        lst.append((y + 1, x))

    return lst


##########################################################
N = int(input())
block = [list(map(int, input().split())) for _ in range(N)]
grid = [[0] * 10 for _ in range(10)]

for y in range(4, 10):
    for x in range(4, 10):
        grid[y][x] = 9
#############################################s#############
score = 0
for i in range(N):
    t, y, x = block[i]
    now_lst = make_coord(t, y, x)

    green = now_lst[:]
    blue = now_lst[:]

    first_move(green, 0)
    first_move(blue, 1)

    # 가득 차있는지 확인하고 조치
    full()

    # 특별한 칸 규칙 적용
    special_rule()
##########################################################
count = 0

for y in range(6, 10):
    for x in range(4):
        if grid[y][x] == 1:
            count += 1

for x in range(6, 10):
    for y in range(4):
        if grid[y][x] == 1:
            count += 1

print(score)
print(count)
