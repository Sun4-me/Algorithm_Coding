import sys

sys.setrecursionlimit(100_002)


def dfs(s):
    v[s] = 1

    for nxt in adj[s]:
        if v[nxt] == 0:
            res[s].append(nxt)
            dfs(nxt)


############################################
# 노드의 개수
N = int(input())
adj = [[] for _ in range(N + 1)]
v = [0] * (N + 1)
nodes = [list(map(int, input().split())) for _ in range(N - 1)]
for i in nodes:
    adj[i[0]].append(i[1])
    adj[i[1]].append(i[0])

# 인덱스가 안에 있는 값의 부모
res = [[] for _ in range(N + 1)]
dfs(1)
############################################
# 정답 배열
ans = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(len(res[i])):
        ans[res[i][j]] = i

# 2부터 슬라이싱
for k in ans[2:]:
    print(k)
