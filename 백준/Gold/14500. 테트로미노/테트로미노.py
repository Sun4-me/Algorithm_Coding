def dfs(depth, sm, path):
    global res

    # 남은 칸이 가장 큰 값만 쏙쏙 골라 더해도 안되면 쳐내기
    if sm + (4 - depth) * max_num <= res:
        return

    # 4칸을 다 선택했으면 return
    if depth == 4:
        res = max(sm, res)
        return

    # 모든 칸에서 상하좌우로..
    for y, x in path:
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]

            if 0 <= ny < N and 0 <= nx < M:
                if not v[ny][nx]:
                    v[ny][nx] = True
                    dfs(depth + 1, sm + grid[ny][nx], path + [(ny, nx)])
                    v[ny][nx] = False

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
#################################################################
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
v = [[False for _ in range(M)] for _ in range(N)]
#################################################################

res = 0
max_num = 0

for row in grid:
    max_num = max(max_num, max(row))

for i in range(N):
    for j in range(M):
        v[i][j] = True
        dfs(1, grid[i][j], [(i, j)])
        v[i][j] = False

print(res)