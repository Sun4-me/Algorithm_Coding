from collections import deque


def bfs(s):
    visited = [0] * (f + 1)
    visited[s] = 1
    q = deque([s])

    while q:
        curr = q.popleft()

        for nxt in (curr + u, curr - d):
            if 0 < nxt <= f:
                if visited[nxt] == 0:
                    visited[nxt] = visited[curr] + 1
                    q.append(nxt)

    return visited[g]


###################################
# F층으로 이루어진 고층 건물에 사무실
# G층에 스타트링크
# S층에 있고 엘베타고 G층으로  이동
# 위로 u만큼 아래로 d만큼 이동

f, s, g, u, d = map(int, input().split())

res = bfs(s)

if res == 0:
    print("use the stairs")
    quit()

print(res - 1)
