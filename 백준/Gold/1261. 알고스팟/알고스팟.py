from heapq import heappop, heappush
from pprint import *

INF = 10 ** 10


def dijkstra(start):
    q = []
    heappush(q, start)

    while q:
        cur_wall, cy, cx = heappop(q)

        # 가지치기 # 목적지에 도달했다면
        if (cy, cx) == (m - 1, n - 1):
            return

        # 가지치기 # 이미 작은 값 있다면
        if wall[cy][cx] < cur_wall:
            continue

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m:

                if grid[ny][nx] == 1:
                    if cur_wall + 1 < wall[ny][nx]:
                        wall[ny][nx] = cur_wall + 1
                        heappush(q, (cur_wall + 1, ny, nx))

                elif grid[ny][nx] == 0:
                    if cur_wall < wall[ny][nx]:
                        wall[ny][nx] = cur_wall
                        heappush(q, (cur_wall, ny, nx))


########################################################
m, n = map(int, input().split())
grid = [list(map(int, input())) for _ in range(n)]
########################################################
start = (0, 0, 0)
wall = [[INF] * m for _ in range(n)]
wall[0][0] = 0
dijkstra(start)
########################################################
print(wall[n - 1][m - 1])
