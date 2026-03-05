from collections import deque

dy = [-2, -2, -1, -1, 1, 1, 2, 2, -1, 1, 0, 0]
dx = [-1, 1, -2, 2, -2, 2, -1, 1, 0, 0, 1, -1]


def bfs():
    power = K

    q = deque([(0, 0, power)])
    v = [[[0] * (K + 1) for _ in range(w)] for _ in range(h)]
    v[0][0][power] = 1

    while q:
        cy, cx, cp = q.popleft()

        if (cy, cx) == (h - 1, w - 1):
            return v[cy][cx][cp] - 1

        for k in range(12):
            np = cp
            use_power = True

            if k in (8, 9, 10, 11):
                use_power = False

            if use_power:
                if cp == 0:
                    continue
                else:
                    np = cp - 1

            ny, nx = cy + dy[k], cx + dx[k]

            if 0 <= ny < h and 0 <= nx < w:
                if grid[ny][nx] == 0:
                    if v[ny][nx][np] == 0:
                        v[ny][nx][np] = v[cy][cx][cp] + 1
                        q.append((ny, nx, np))

    return -1


#########################################################


K = int(input())
w, h = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]
#########################################################
ans = bfs()

print(ans)
