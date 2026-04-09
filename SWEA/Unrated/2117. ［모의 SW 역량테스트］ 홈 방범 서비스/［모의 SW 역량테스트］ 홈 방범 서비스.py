# ---------------------------------------------------------------------
 
def inb(y, x):
    return 0 <= y < N and 0 <= x < N
 
 
def dist(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)
 
 
def cost(k):
    return k * k + (k - 1) * (k - 1)
 
 
# ---------------------------------------------------------------------
T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    homes = [list(map(int, input().split())) for _ in range(N)]
 
    ans = 0
 
    for k in range(N + 2):
        for cy in range(N):
            for cx in range(N):
                now_operate_cost = cost(k)
                now_home_cnt = 0
 
                for y in range(cy - (k - 1), cy + k):
                    for x in range(cx - (k - 1), cx + k):
                        if not inb(y, x): continue
                        if not dist(cy, cx, y, x) <= k - 1: continue
                        if homes[y][x] == 1: now_home_cnt += 1
 
                if now_home_cnt * M - now_operate_cost >= 0:
                    ans = max(ans, now_home_cnt)
 
    print(f"#{case} {ans}")