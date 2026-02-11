from heapq import heappop, heappush

INF = 10 ** 10


def dijkstra(s):
    q = []
    heappush(q, s)

    while q:
        cur_dist, cur_node = heappop(q)

        if distance[cur_node] < cur_dist:
            continue

        for weight, nxt_node in adj[cur_node]:
            dist = cur_dist + weight

            if dist < distance[nxt_node]:
                distance[nxt_node] = dist
                heappush(q, (dist, nxt_node))


# d = (집-KIST의 최단 거리) + (집-씨알푸드의 최단 거리)
#############################################
N, V, E = map(int, input().split())
A, B = map(int, input().split())
houses = list(map(int, input().split()))
adj = [[] for _ in range(E + 1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))
    adj[e].append((w, s))
#############################################
# 초기값
res = [0] * (E + 1)
START = [A, B]
for i in START:
    distance = [INF] * (E + 1)
    distance[i] = 0
    s = (0, i)
    dijkstra(s)
    for j in range(E):
        if distance[j] != INF:
            res[j] += distance[j]
        else:
            res[j] += -1

ans = 0
for i in houses:
    ans += res[i]

print(ans)
