from collections import deque

qwerty = [
    "QWERTYUIOP",
    "ASDFGHJKL",
    "ZXCVBNM"
]

# 문자 위치 저장
pos = {}
for i in range(len(qwerty)):
    for j in range(len(qwerty[i])):
        pos[qwerty[i][j]] = (i, j)

# 상 하 좌 우 대상우 대하좌
direct = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1),
    (-1, 1), (1, -1)
]


def bfs(s, e):
    if s == e:
        return 0

    s_pos = pos[s]
    e_pos = pos[e]

    # 좌표랑 거리 같이 담기
    q = deque([(s_pos, 0)])
    # set으로 관리 해보자
    visited = {s_pos}

    while q:
        (cy, cx), dist = q.popleft()

        if (cy, cx) == e_pos:
            return dist

        for dy, dx in direct:
            ny, nx = cy + dy, cx + dx

            if 0 <= ny < 3 and 0 <= nx < len(qwerty[ny]):
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    q.append(((ny, nx), dist + 1))


t = int(input())

for _ in range(t):
    s = input()

    ans = 1

    for i in range(1, len(s)):
        dist = bfs(s[i - 1], s[i])
        # 거리 + 누르는 시간
        ans += (dist * 2) + 1

    print(ans)
