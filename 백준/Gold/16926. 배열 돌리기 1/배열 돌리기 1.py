from collections import deque

N, M, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 돌려야하는 테두리 갯수
cnt = min(N, M) // 2

nxt_grid = [[0] * M for _ in range(N)]

for step in range(cnt):
    q = deque()
    nums = []

    # 왼쪽면
    for y in range(step, N - step):
        q.append((y, step))
        nums.append(grid[y][step])

    # 아랫면
    for x in range(1 + step, M - 1 - step):
        q.append((N - 1 - step, x))
        nums.append(grid[N - 1 - step][x])

    # 오른쪽면
    for y in range(N - 1 - step, -1 + step, -1):
        q.append((y, M - 1 - step))
        nums.append(grid[y][M - 1 - step])

    # 윗면
    for x in range(M - 2 - step, step, -1):
        q.append((step, x))
        nums.append(grid[step][x])

    q.rotate(-R)

    for i in range(len(q)):
        y, x = q[i]
        num = nums[i]
        nxt_grid[y][x] = num

for row in nxt_grid:
    print(*row, sep=" ")
