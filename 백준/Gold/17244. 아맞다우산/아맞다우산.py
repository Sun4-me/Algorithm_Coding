from collections import deque


def bfs(y, x):
    q = deque([(y, x, 0)])
    v[y][x][0] = 1

    # 모든 물건을 주웠을 때의 최종 비트마스크 값
    target_mask = (1 << x_cnt) - 1

    while q:
        cy, cx, mask = q.popleft()

        if mask == target_mask and (cy, cx) == (ey, ex):
            return v[cy][cx][mask] - 1

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx

            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx] != "#":
                    next_mask = mask

                    # 만약 다음 칸이 물건(X)이라면 비트마스크 갱신
                    if grid[ny][nx] == "X":
                        bit_idx = x_dict[(ny, nx)]  # 이 물건의 고유 번호 가져오기
                        next_mask = mask | (1 << bit_idx)  # 해당 물건 비트 켜기

                    # 해당 상태로 다음 칸에 방문한 적이 없다면
                    if not v[ny][nx][next_mask]:
                        v[ny][nx][next_mask] = v[cy][cx][mask] + 1
                        q.append((ny, nx, next_mask))

    return 0


m, n = map(int, input().split())
grid = [list(input()) for _ in range(n)]

sy, sx, ey, ex = -1, -1, -1, -1
x_cnt = 0
x_dict = {}

for y in range(n):
    for x in range(m):
        if grid[y][x] == "S":
            sy, sx = y, x
        elif grid[y][x] == "E":
            ey, ex = y, x
        elif grid[y][x] == "X":
            x_dict[(y, x)] = x_cnt
            x_cnt += 1

# 비트마스크 상태 개수(1 << x_cnt)만큼 생성
v = [[[0] * (1 << x_cnt) for _ in range(m)] for _ in range(n)]

ans = bfs(sy, sx)

print(ans)