from heapq import heappop, heappush
# from pprint import *

INF = 10 ** 10


def dijkstra(start):
    q = []
    heappush(q, start)

    while q:
        cur_cost, cy, cx = heappop(q)

        if (cy, cx) == (y2 - 1, x2 - 1):
            return

        if cost[cy][cx] < cur_cost:
            continue

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m:

                if grid[ny][nx] == '1':
                    if cur_cost + 1 < cost[ny][nx]:
                        cost[ny][nx] = cur_cost + 1
                        heappush(q, (cur_cost + 1, ny, nx))

                else:
                    if cur_cost < cost[ny][nx]:
                        cost[ny][nx] = cur_cost
                        heappush(q, (cur_cost, ny, nx))


########################################################
n, m = map(int, input().split())
y1, x1, y2, x2 = map(int, input().split())
grid = [list(input()) for _ in range(n)]
########################################################
start = (0, y1 - 1, x1 - 1)
cost = [[INF] * m for _ in range(n)]
cost[y1 - 1][x1 - 1] = 0
dijkstra(start)
########################################################
print(cost[y2 - 1][x2 - 1] + 1)
