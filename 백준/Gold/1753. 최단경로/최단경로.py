from heapq import heappop, heappush

INF = 10 ** 10


def dijktra(start):
    q = []
    heappush(q, (0, start))

    while q:
        c_w, c_p = heappop(q)

        if v[c_p] < c_w:
            continue

        for n_w, n_p in adj[c_p]:
            dist = c_w + n_w
            if dist < v[n_p]:
                v[n_p] = dist
                heappush(q, (dist, n_p))


# 1부터 v까지
V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]
start = int(input())
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

v = [INF] * (V + 1)
v[start] = 0
dijktra(start)

for i in range(1, V + 1):
    res = v[i]
    if res == 10 ** 10:
        res = "INF"

    print(res)
