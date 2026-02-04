def dist(lst1, lst2):
    return abs(lst1[0] - lst2[0]) + abs(lst1[1] - lst2[1])


def dfs(depth, s, lst):
    global res

    if depth == K:
        max_dist = 0
        for j in range(N):
            min_dist = 1000000
            for i in range(K):
                min_dist = min(min_dist, dist(lst[i], houses[j]))
            max_dist = max(min_dist, max_dist)
        res = min(res, max_dist)
        return

    for i in range(s, N):
        dfs(depth + 1, i + 1, lst + [houses[i]])


# N개 중에 K개 선택해야 함
# 순서 상관 없음
N, K = map(int, input().split())

# X, Y
houses = [list(map(int, input().split())) for _ in range(N)]

res = 1000000
dfs(0, 0, [])
print(res)
