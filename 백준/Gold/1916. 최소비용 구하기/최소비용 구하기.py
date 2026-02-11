from heapq import heappop, heappush

INF = 10 ** 10


def dijkstra(s):
    q = []
    heappush(q, s)

    while q:
        cur_dist, cur_node = heappop(q)

        # HEAP 이니까 종료 노드 마주치는 순간 최단거리임
        if cur_node == END:
            return

        # 이미 더 작은 거리가 들어 있다면 PASS
        if distance[cur_node] < cur_dist:
            continue

        for weight, nxt_node in adj[cur_node]:
            dist = cur_dist + weight

            # 새로 만든 거리가 기존에 있는것 보다 작다면
            if dist < distance[nxt_node]:
                distance[nxt_node] = dist
                heappush(q, (dist, nxt_node))


#############################################
N = int(input())
M = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))
# 시작, 목표
START, END = map(int, input().split())
#############################################
# 초기값
distance = [INF] * (N + 1)
distance[START] = 0
s = (0, START)

dijkstra(s)
print(distance[END])
