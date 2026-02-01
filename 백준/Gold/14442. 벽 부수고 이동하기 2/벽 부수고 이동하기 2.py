from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    # v[y][x][0]: 벽 안 부숨, v[y][x][k]: k개 벽 부숨
    v = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
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

                # 이동할 곳이 벽이고, 아직 벽을 k번 부순적이 없고 방문한적이 없을 때
                elif grid[ny][nx] == 1 and state < k:
                    if v[ny][nx][state + 1] == 0:
                        v[ny][nx][state + 1] = v[cy][cx][state] + 1
                        q.append((ny, nx, state + 1))

    return -1


#####################################################
n, m, k = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
#####################################################
print(bfs())
#####################################################
