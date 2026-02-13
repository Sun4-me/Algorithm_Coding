# from pprint import *

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, -2, -1, 1, 2]


def dfs(depth, sm):
    global ans

    ans = max(ans, sm)

    for row in range(n):
        for col in range(n):
            if v[row][col] == 0:

                for k in range(8):
                    ny, nx = row + dy[k], col + dx[k]
                    if 0 <= ny < n and 0 <= nx < n:
                        if v[ny][nx] == 1:
                            break
                else:
                    v[row][col] = 1
                    dfs(depth + 1, sm + grid[row][col])
                    v[row][col] = 0


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
v = [[0] * n for _ in range(n)]
dfs(0, 0)

print(ans)
