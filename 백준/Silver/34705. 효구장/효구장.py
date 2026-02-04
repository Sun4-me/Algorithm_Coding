def dfs(depth, sm):
    global can
    if sm > y:
        return

    if depth == 5:
        if x <= sm:
            can = True
        return

    dfs(depth + 1, sm + weight[depth])
    dfs(depth + 1, sm)


##################################################
t = int(input())
for case in range(t):
    x, y = map(int, input().split())
    weight = list(map(int, input().split()))

    can = False
    dfs(0, 0)
    print("YES" if can else "NO")
