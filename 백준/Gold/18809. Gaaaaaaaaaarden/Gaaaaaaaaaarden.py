from collections import deque
from itertools import combinations


def bfs():
    v = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for y, x, s in q:
        v[y][x][s] = 1

    v_set = set()

    while q:
        cy, cx, state = q.popleft()

        if v[cy][cx][0] != 0 and v[cy][cx][0] == v[cy][cx][1]:
            if (cy, cx) not in v_set:
                cnt += 1
                v_set.add((cy, cx))
            continue

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if grid[ny][nx] != 0:
                    if v[ny][nx][state] == 0:
                        v[ny][nx][state] = v[cy][cx][state] + 1
                        q.append((ny, nx, state))

    return cnt


n, m, g, r = map(int, input().split())
# 0: 호수, 1: 배양액 x, 2: 배양액 O
grid = [list(map(int, input().split())) for _ in range(n)]

possible = [(y, x) for y in range(n) for x in range(m) if grid[y][x] == 2]

ans = 0

for combi in combinations(possible, g + r):
    for i in combinations(combi, g):
        q = deque()

        for y, x in i:
            # 그린은 0
            q.append((y, x, 0))

        for y, x in combi:
            # 레드는 1
            if (y, x, 0) not in q:
                q.append((y, x, 1))

        res = bfs()

        ans = max(ans, res)

print(ans)
