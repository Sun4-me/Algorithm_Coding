from collections import deque


################################################

def bfs(s):
    visited = [0] * (n + 1)
    visited[s] = 1
    cnt = 1
    q = deque([s])

    while q:
        c = q.popleft()

        for nxt in adj[c]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                cnt += 1
                q.append(nxt)

    return cnt


################################################
n, m = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(m)]
################################################
# 신뢰하는 방향의 반대 방향으로 번호가 이동이 가능함
adj = [[] for _ in range(n + 1)]
for row in nodes:
    adj[row[1]].append(row[0])
################################################
# 모든 번호를 돌리고자 하는데, visit이 0인 경우만 하면 안됨..
# 모든 번호를 돌리면 시간, 메모리 초과가 안날까? -> 날 거 같음
# 다른 방법 생각해보자..?
# 생각 안나요.. 될 것 같아요 기세로 넣어봅시다
# 틀릴 용기..
# ....?
# 시간초과랑 메모리 우려했는데 문제를 틀려버림 ㅜ.ㅜ
# 최소거리가 아니라 방문횟수를 세어야 했음 !
# 최소인 경우 맥스인 경우, 서로 양방향인 경우 등 테케를 더 완벽히 해보자
res = []
for num in range(1, n + 1):
    res.append(bfs(num))
################################################
max_num = max(res)
for i in range(n):
    if res[i] == max_num:
        print(i + 1, end=" ")
################################################
