# 이동한 칸에 쓰여 있는 수가 0이면, 주사위 바닥면에 쓰여있는 수가 칸에 복사
# 0이 아니면 주사위의 바닥면으로 복사. 칸은 0이 됨
# 세로 크기, 가로 크기
from collections import deque
from pprint import *

# 동 서 북 남
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


def move(cy, cx, d):
    ny, nx = cy + dy[d - 1], cx + dx[d - 1]

    if grid[ny][nx] != -1:  # 범위 안이라면,
        # 동쪽, 남쪽
        if d == 1 or d == 4:
            direction = 1  # 제일 앞에 있던 것 뒤로
        # 서쪽, 북쪽
        else:
            direction = -1  # 제일 뒤에 있던 것 앞으로

        # 동쪽, 서쪽
        if d == 1 or d == 2:
            lst = left_right
            opponent = up_down
        # 북쪽, 남쪽
        else:
            lst = up_down
            opponent = left_right
        #######################################################
        # 현재 리스트 처리
        down = visit_grid(lst, ny, nx, direction)  # 갱신 할 바닥면
        lst.rotate(direction)  # 방향에 따라 다르게 rotate
        lst.pop()  # 지금 현재 바닥은 뺌
        lst.append(down)  # 주사위의 바닥 면 갱신
        up = lst[1]  # 주사위의 현재 윗면
        #######################################################
        # ! KEY POINT !
        # 반대 리스트 처리 | 위, 아래만 갱신해주면 끝
        opponent[1] = up
        opponent[3] = down
        # 현재 위쪽 면 출력
        print(up)
        return ny, nx

    # 이동하지 못한다면 현재위치 그대로 반환
    return cy, cx


# 칸 처리, 주사위의 적을 수 반환
def visit_grid(lst, ny, nx, d):
    # 칸이 0이라면
    if grid[ny][nx] == 0:
        # 방향에 따라 다르기 때문에
        # 동쪽, 남쪽
        if d == 1:
            grid[ny][nx] = lst[2]
            return lst[2]
        # 서쪽, 북쪽
        else:
            grid[ny][nx] = lst[0]
            return lst[0]
    # 칸이 0이 아니라면
    else:
        # 칸의 수
        num = grid[ny][nx]
        grid[ny][nx] = 0
        return num


##################################################################
# 입력
n, m, x, y, k = map(int, input().split())
original_grid = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
##################################################################
# 패딩
minus_row = [[-1] * (m + 2)]
middle_row = [[-1] + row + [-1] for row in original_grid]
grid = minus_row + middle_row + minus_row
##################################################################
# 패딩에 따른 조정
n, m = n + 2, m + 2
x, y = x + 1, y + 1
##################################################################
# 북 위 남 아래
up_down = deque([0, 0, 0, 0])
# 서 위 동 아래
left_right = deque([0, 0, 0, 0])
##################################################################
for cmd in command:
    # x랑 y를 반대로 줬음 레전드 악질 주의 (범위 보고 제대로 봐야 함)
    x, y = move(x, y, cmd)
