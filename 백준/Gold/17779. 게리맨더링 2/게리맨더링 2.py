# [선거구 구역 조건]
# [1] 다섯개 선거구로 나눌 것
# [2] 구역을 적어도 하나 포함하고 한 선건구 안은 모두 연결되어 있어야 할 것
from collections import deque


def inb(x, y):
    return 0 <= x < N and 0 <= y < N


def inb_diagonal(x, y, d1, d2):
    """현재 좌표에서 가능한 대각선인가?"""
    return 0 <= x < x + d1 + d2 < N and 0 <= y - d1 < y < y + d2 < N


def make_direct(x, y, d1, d2):
    """경계선 만들고 경계선 좌표 리턴"""

    lst_1 = [(x + k, y - k) for k in range(d1 + 1)]
    lst_2 = [(x + k, y + k) for k in range(d2 + 1)]
    lst_3 = [(x + d1 + k, y - d1 + k) for k in range(d2 + 1)]
    lst_4 = [(x + d2 + k, y + d2 - k) for k in range(d1 + 1)]

    return [lst_1] + [lst_2] + [lst_3] + [lst_4]


def marking(coord):
    """선거구를 나누고 v에 마킹하기"""
    v = [[0] * N for _ in range(N)]

    # 전체 구역 색칠하자
    top, bottom, left, right = coord[0][0], coord[3][-1], coord[2][0], coord[3][0]

    for x in range(top[0]):
        v[x][top[1]] = 1

    for x in range(bottom[0], N):
        v[x][bottom[1]] = 4

    for y in range(left[1]):
        v[left[0]][y] = 3

    for y in range(right[1], N):
        v[right[0]][y] = 2

    # 경계선 덧칠
    for k in coord:
        for x, y in k:
            v[x][y] = 5

    # 번호 칠하기

    q = deque([(0, 0, 1), (0, N - 1, 2), (N - 1, 0, 3), (N - 1, N - 1, 4)])

    v[0][0] = 1
    v[0][N - 1] = 2
    v[N - 1][0] = 3
    v[N - 1][N - 1] = 4

    while q:
        cx, cy, c_num = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = cx + dx, cy + dy
            if inb(nx, ny):
                if v[nx][ny] == 0:
                    v[nx][ny] = c_num
                    q.append((nx, ny, c_num))

    return v


def cal(v):
    """인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값 리턴"""
    lst = [0, 0, 0, 0, 0]

    for x in range(N):
        for y in range(N):
            if v[x][y] == 1:
                lst[0] += grid[x][y]

            elif v[x][y] == 2:
                lst[1] += grid[x][y]

            elif v[x][y] == 3:
                lst[2] += grid[x][y]

            elif v[x][y] == 4:
                lst[3] += grid[x][y]

            elif v[x][y] == 5 or v[x][y] == 0:
                lst[4] += grid[x][y]

    return max(lst) - min(lst)


############################################################
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
############################################################
ans = 10 ** 10

for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):

                # 가능하지 않은 조합이면 pass
                if not inb_diagonal(x, y, d1, d2):
                    continue

                # 경계선 제작
                coord = make_direct(x, y, d1, d2)

                # 구역 나눔 제작
                v = marking(coord)

                # 최솟값 중의 최솟값 찾기
                ans = min(ans, cal(v))
############################################################
print(ans)
