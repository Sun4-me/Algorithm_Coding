from collections import deque
from pprint import *


def bfs():
    # v[y][x][0]: 벽 안 부숨, v[y][x][1]: 벽 부숨
    # z, y, x 형식이 아니라 y, x 에서의 0번째 1번째 !
    # 2차원에서 공유하면서 갱신하면 벽을 이미 부순 경로가 먼저 도착한 경우
    # 늦게 도착한 벽을 한 번도 안 부순 경로는 갱신을 하지 못함..
    # 근데 얘는 목적지에 도달할 유일한 애였을 수도 있음..
    # 따라서 나눠서 관리를 해야함
    v = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    v[0][0][0] = 1

    q = deque([(0, 0, 0)])

    while q:
        cy, cx, state = q.popleft()

        if cy == n - 1 and cx == m - 1:
            return v[cy][cx][state]

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx

            if 0 <= ny < n and 0 <= nx < m:
                # 이동할 곳이 빈칸이고 해당 상태로 방문한적이 없을 때
                if grid[ny][nx] == 0 and v[ny][nx][state] == 0:
                    v[ny][nx][state] = v[cy][cx][state] + 1
                    q.append((ny, nx, state))

                # 이동할 곳이 벽이고, 아직 벽을 부순적이 없고 방문한적이 없을 때
                elif grid[ny][nx] == 1 and state == 0:
                    if v[ny][nx][1] == 0:
                        v[ny][nx][1] = v[cy][cx][0] + 1
                        q.append((ny, nx, 1))

    return -1


#####################################################
n, m = map(int, input().split())
grid = [list(map(int, input())) for _ in range(n)]
#####################################################
print(bfs())
#####################################################
