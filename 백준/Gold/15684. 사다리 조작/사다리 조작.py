from itertools import combinations


def go(idx):
    cy, cx = 0, idx

    while True:
        if not 0 <= cy < H + 1 and 1 <= cx < N + 1:
            break

        if adj[cy][cx] == 0:
            cy, cx = cy + 1, cx

        else:
            cy, cx = cy + 1, adj[cy][cx]

    if cx == idx:
        return True

    else:
        return False


###############################################################
# 세로선의 개수, 가로선의 개수, 세로선마다 가로선을 놓을 수 있는 위치의 개수
N, M, H = map(int, input().split())
adj = [[0] * (N + 1) for _ in range(H + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = b + 1
    adj[a][b + 1] = b
###############################################################
possible_1 = []

# 1개짜리 가로선
for y in range(1, H + 1):
    for x in range(1, N):
        if adj[y][x] == 0 and adj[y][x + 1] == 0:
            possible_1.append((y, x))


possible_2 = []

# 2짜리 가로선
# 1개짜리 가로선
for combi in combinations(possible_1, 2):
    if combi[0][0] == combi[1][0]:
        if combi[0][1] + 1 == combi[1][1]:
            continue

        if combi[1][1] + 1 == combi[0][1]:
            continue

    possible_2.append(combi)

possible_3 = []
for combi in combinations(possible_1, 3):
    if combi[0][0] == combi[1][0]:
        if combi[0][1] + 1 == combi[1][1]:
            continue

        if combi[1][1] + 1 == combi[0][1]:
            continue

    if combi[1][0] == combi[2][0]:
        if combi[1][1] + 1 == combi[2][1]:
            continue

        if combi[2][1] + 1 == combi[1][1]:
            continue

    if combi[0][0] == combi[2][0]:
        if combi[0][1] + 1 == combi[2][1]:
            continue

        if combi[2][1] + 1 == combi[0][1]:
            continue

    possible_3.append(combi)
###############################################################
flag = False
ans = -1

# [0] 사다리 하나도 안 만들어도 가능한지 확인.
for i in range(1, N + 1):
    if not go(i):
        break

else:
    flag = True
    ans = 0
###############################################################
# [1] 사다리 한개의 경우.
for y, x in possible_1:
    if flag:
        break

    adj[y][x] = x + 1
    adj[y][x + 1] = x

    for i in range(1, N + 1):
        if not go(i):
            break

    else:
        flag = True
        ans = 1

    adj[y][x] = 0
    adj[y][x + 1] = 0

# [2] 사다리 두개의 경우.
for j in possible_2:
    if flag:
        break
    for y, x in j:
        adj[y][x] = x + 1
        adj[y][x + 1] = x

    for i in range(1, N + 1):
        if not go(i):
            break

    else:
        flag = True
        ans = 2


    for y, x in j:
        adj[y][x] = 0
        adj[y][x + 1] = 0

# [3] 사다리 세개의 경우.
for j in possible_3:
    if flag:
        break
    for y, x in j:
        adj[y][x] = x + 1
        adj[y][x + 1] = x

    for i in range(1, N + 1):
        if not go(i):
            break

    else:

        flag = True
        ans = 3

    for y, x in j:
        adj[y][x] = 0
        adj[y][x + 1] = 0

print(ans)


