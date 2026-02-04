# N+1에 퇴사 N일 동안 최대한 많은 상담
# 상담을 완료하는데 걸리는 시간 Ti,
# 상담을 했을때 받을 수 있는 금액 Pi,

# 깊이, 상담 중, 현재 상담 완료 하면 받을 금액, 이익
def dfs(depth, sm):
    global res

    if depth <= N:
        if sm > res:
            res = sm

    for i in range(depth, N):
        if i + nodes[i][0] <= N:
            dfs(i + nodes[i][0], sm + nodes[i][1])


##################################################
N = int(input())
nodes = [list(map(int, input().split())) for _ in range(N)]

v = [0] * N
res = 0
dfs(0, 0)

print(res)
