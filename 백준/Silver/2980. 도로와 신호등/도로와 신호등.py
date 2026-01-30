#########################################################
n, l = map(int, input().split())
# d, r, g
nodes = [list(map(int, input().split())) for _ in range(n)]
#########################################################
dist = 1
cnt = 1
idx = 0
cycle = 0
#########################################################
while True:

    if dist == l:
        break

    elif idx < n:
        if dist == nodes[idx][0]:
            cycle = nodes[idx][1] + nodes[idx][2]
            wait = nodes[idx][1] - (cnt % cycle)

            if wait > 0:
                cnt += wait

            idx += 1

    dist += 1
    cnt += 1
print(cnt)
