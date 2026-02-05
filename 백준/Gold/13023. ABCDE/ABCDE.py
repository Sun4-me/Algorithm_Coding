def dfs(depth, s):
    global can

    if depth == 5:
        can = 1
        return

    for nxt in relations[s]:
        if v[nxt] == 0:
            v[nxt] = 1
            dfs(depth + 1, nxt)
            v[nxt] = 0


##########################################
n, m = map(int, input().split())
relations = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)
##########################################
v = [0] * n
can = 0
v[0] = 1

for k in range(n):
    v[k] = 1
    dfs(1, k)
    v[k] = 0

print(can)
