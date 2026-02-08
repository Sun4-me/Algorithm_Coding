# S가 최소 넷
# 즉 Y가 4면 안됨
# 4인 경우의 수 모으고 - 그 좌표가 이동 위치로 구성 되어 있는지 확인 하자
# 이터툴로 풀어보기
from collections import deque
from itertools import combinations


def bfs():
    v = set(lst)

    q = deque([lst[0]])
    cnt = 1

    v.remove(lst[0])

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if (ny, nx) in v:
                v.remove((ny, nx))
                cnt += 1
                q.append((ny, nx))

    return 1 if cnt == 7 else 0


grid = [list(input()) for _ in range(5)]
ans = 0

for comb in combinations(range(25), 7):
    y_cnt = 0
    lst = []

    for idx in comb:
        y = idx // 5
        x = idx % 5
        lst.append((y, x))

        if grid[y][x] == 'Y':
            y_cnt += 1

    if y_cnt >= 4:
        continue

    if bfs():
        ans += 1

print(ans)
