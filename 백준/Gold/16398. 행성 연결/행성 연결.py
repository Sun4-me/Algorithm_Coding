def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        p[y] = x

    else:
        p[x] = y


n = int(input())
edges = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] != 0:
            edges.append((line[j], i, j))

edges.sort(key=lambda x: x[0])
p = [i for i in range(n + 1)]

cost = 0
for w, s, e in edges:
    if find(s) != find(e):
        union(s, e)
        cost += w

print(cost)