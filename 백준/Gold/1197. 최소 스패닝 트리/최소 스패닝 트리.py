from heapq import heappop, heappush


def prime(s):
    global ans
    q = []
    heappush(q, s)
    v = [0] * (V + 1)

    while q:
        cur_weight, cur_node = heappop(q)

        # 이미 방문했으면 안봐도 됨
        if v[cur_node] == 1:
            continue

        # 방문처리 및 가중치 합산
        v[cur_node] = 1
        ans += cur_weight

        for nxt_weight, nxt_node in adj[cur_node]:
            # 방문안했다면 넣어줌
            if not v[nxt_node]:
                heappush(q, (nxt_weight, nxt_node))


V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))
    adj[e].append((w, s))

start = (0, 1)
ans = 0

prime(start)
print(ans)
