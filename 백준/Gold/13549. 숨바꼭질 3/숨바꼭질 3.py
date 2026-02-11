from heapq import heappop, heappush


def dijkstra():
    global n, k
    q = []
    # 비용 = 시간
    heappush(q, (0, n))

    while q:
        curr_weight, curr_loc = heappop(q)

        if distance[curr_loc] < curr_weight:
            continue

        # 무조건 최단 거리
        if curr_loc == k:
            return curr_weight

        for nxt_weight, nxt_loc in ((0, curr_loc * 2), (1, curr_loc - 1), (1, curr_loc + 1)):
            if 0 <= nxt_loc <= 100000:
                if curr_weight + nxt_weight < distance[nxt_loc]:
                    # 방만하다 nxt_loc을 curr_loc으로 했다..
                    distance[nxt_loc] = curr_weight + nxt_weight
                    heappush(q, (curr_weight + nxt_weight, nxt_loc))


n, k = map(int, input().split())
INF = 10 ** 10
distance = [INF] * 100001
time = dijkstra()

print(time)
