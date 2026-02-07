# 하얀 사각형은 점프할 때마다 다양한 색의 잉크를 뿌림
# 뿌려진 잉크는 투명한 장애물에 부딪혀 투명했던 장애물 염색
# 이제 플레이어는 염색된 장애물 볼 수 있음
# 칸은 빈칸 or 장애물
# 커맨드 k번
from collections import deque

# 0:상, 1:하, 2:좌, 3:우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
direct = ['U', 'D', 'L', 'R']


#############################################
# 이동 커맨드
def move(cy, cx, k):
    ny, nx = cy + dy[k], cx + dx[k]

    if grid[ny][nx] == '.':
        grid[cy][cx] = '.'
        grid[ny][nx] = '@'
        return ny, nx

    return cy, cx


#############################################
# 잉크 충천 커맨드
def charge():
    global ink_amount
    ink_amount += 1
    return


#############################################
# 점프 커맨드
def jump(y, x):
    v = [[0] * (n + 2) for _ in range(n + 2)]
    v[y][x] = 1
    color = ink[jump_count % i]
    q = deque([(y, x)])

    while q:
        cy, cx = q.popleft()

        for k in range(4):
            ny, nx = cy + dy[k], cx + dx[k]
            # 예스 장애물 or color, 낫 방문, 잉크양 이하의 거리
            if v[cy][cx] <= ink_amount:
                if grid[ny][nx] != '|' and v[ny][nx] == 0:
                    v[ny][nx] = v[cy][cx] + 1
                    if grid[ny][nx] != '.':
                        if v[ny][nx] <= ink_amount + 1:
                            grid[ny][nx] = color
                    q.append((ny, nx))


#############################################
i, n, k = map(int, input().split())
ink = input()
original_grid = [list(input()) for _ in range(n)]
command = input()

top_down = [['|'] * (n + 2)]
middle_row = [['|'] + row + ['|'] for row in original_grid]
grid = top_down + middle_row + top_down
#############################################
ink_amount = 0  # 잉크의 양
jump_count = 0  # 점프 횟수
#############################################
cy, cx = -1, -1
# 사각형 위치 찾기
for row in range(n + 2):
    for col in range(n + 2):
        if grid[row][col] == '@':
            cy, cx = row, col
            break
#############################################
for cmd in command:
    if cmd in direct:
        cy, cx = move(cy, cx, direct.index(cmd))

    elif cmd == 'j':
        charge()

    elif cmd == 'J':
        jump(cy, cx)
        ink_amount = 0
        jump_count += 1


for row in grid[1: -1]:
    print(*row[1:-1], sep="")
