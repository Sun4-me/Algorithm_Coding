def dfs(depth, s):
    global min_dist
    if depth == m:
        sm = 0 # 도시의 치킨 거리
        for i in range(len(houses)):
            tmp = 10 ** 8
            for j in range(m):
                # 각집의 치킨 거리 중 가장 작은 것
                tmp = min(tmp, dist(houses[i], now_chicken[j]))
            sm += tmp
        min_dist = min(min_dist, sm)
        return

    for i in range(s, len(chicken)):
        now_chicken.append(chicken[i])
        dfs(depth + 1, i + 1)
        now_chicken.pop()


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# r,c는 1부터 시작 주의..
# 집가 가장 가까운 치킨집 거리 = 치킨 거리
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합
# 0은 빈칸, 1은 집, 2는 치킨집
# 최대 M개 고르고 나머지 폐업
# 치킨거리가 가장 작게 되도록 해야함

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
##############################################################
houses = []
chicken = []
for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            houses.append((row, col))
        elif grid[row][col] == 2:
            chicken.append((row, col))
##############################################################
now_chicken = []
min_dist = 10 ** 8
dfs(0, 0)
##############################################################
print(min_dist)