from collections import deque

# 우 하 좌 상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


###################################################################
def inb(y, x):
    return 0 <= y < N and 0 <= x < N


def is_valid(y, x):
    """ 종료 조건
        벽이나 자기 자신이면 False, 아니면 True"""

    # 벽이라면
    if not inb(y, x):
        return False

    # 자기 몸뚱아리라면
    if (y, x) in snake:
        return False

    return True


def is_apple(y, x):
    """사과가 있다면 True"""

    if (y, x) in apples:
        return True

    return False


def is_apple_action(y, x):
    """ 사과가 있을 때 행동 요령
        사과 없애기             """
    apples.remove((y, x))


def not_apple_action(y, x):
    """ 사과가 없을 때 행동 요령
        꼬리가 위치한 칸 비워준다  """
    snake.popleft()


def move(y, x):
    """머리를 다음 칸에 위치 시키기"""
    snake.append((y, x))


###################################################################
# 보드 크기
N = int(input())
# 사과 개수
K = int(input())
# 사과 위치
apples = set()
for _ in range(K):
    y, x = map(int, input().split())
    apples.add((y - 1, x - 1))  # 맨 위 맨 좌측은 1행 1열이므로

# 뱀의 방향 변환 횟수
L = int(input())
# 뱀의 방향 변환 정보 (x, c) x초 뒤에 c방향으로 회전
command_dict = {}
for _ in range(L):
    lines = input().split()
    command_dict[int(lines[0])] = lines[1]
###################################################################
# 뱀 몸 좌표 관리
snake = deque([(0, 0)])

# 뱀의 초기 방향
d = 0
###################################################################
# 게임 진행
time = 0

while True:
    # 방향 설정
    if time in command_dict.keys():
        if command_dict[time] == "D":
            d = (d + 1) % 4
        elif command_dict[time] == "L":
            d = (d - 1) % 4

    # 현재 머리 위치
    cy, cx = snake[-1]

    # 다음 갈 곳
    ny, nx = cy + dy[d], cx + dx[d]

    # [2] 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    # 2번이지만 먼저 수행한다.
    # 종료 조건
    if not is_valid(ny, nx):
        break

    # [1] 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    move(ny, nx)

    # [3] 이동할 칸에 사과가 있는가?
    if is_apple(ny, nx):
        # [3-1] 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        is_apple_action(ny, nx)

    else:
        # [3-2] 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
        not_apple_action(ny, nx)

    time += 1
###################################################################
print(time + 1)
