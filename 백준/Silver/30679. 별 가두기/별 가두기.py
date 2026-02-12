# 첫 스타트는 항상 오른쪽을 봄
# 현재 위치의 칸 수 만큼, 바라보고 있는 방향으로 이동
# 도착하고 나서는 보는 방향을 시계방향 90도 회전
# 격자 밖으로 가려는 순간 실패임
# 무한히 도는 순간 성공
# -> 아이디어: V배열에 도착하고 돌린 방향만 저장해두고
# 나중에 또 도착하고 돌린 방향이 그 곳안에 존재한다면 가둔거다
# 올려둘 수 있는 칸 수와 있다면
# 그 칸들이 몇번 째 행에 있는지 오름차순으로!
# 문제를 잘 읽자...........
# 문제를 잘 읽자...........
# 문제를 잘 읽자...........
# 문제를 잘 읽자...........
# 첫 번째 열의 원하는 칸이다...............................
# 문제를 잘 읽자...........
# 문제를 잘 읽자...........
# 문제를 잘 읽자...........
# 문제를 잘 읽자...........

from pprint import *

# 0:상, 1:우, 2:하, 3:좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def inb(y, x):
    return 0 <= y < n and 0 <= x < m


def start(cy, cx):
    sy, sx = cy, cx
    v = [[[] for _ in range(m)] for _ in range(n)]
    v[cy][cx].append(1)

    d = 1  # 초기 값 오른쪽
    step = grid[cy][cx]

    while True:
        if step == 0:
            step = grid[cy][cx]
            d = (d + 1) % 4
            if d in v[cy][cx]:
                res.append((sy + 1))
                return
            else:
                v[cy][cx].append(d)

        ny, nx = cy + dy[d], cx + dx[d]
        if not inb(ny, nx):
            return

        step -= 1
        cy, cx = ny, nx


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

res = []

for y in range(n):
    start(y, 0)

res.sort()
print(len(res))
print(*res)
