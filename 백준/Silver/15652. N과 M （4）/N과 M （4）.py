def dfs(depth, s):
    if depth == m:
        print(*lst)
        return

    for i in range(s, n+1):
        lst.append(i)
        dfs(depth + 1, i)
        lst.pop()


n, m = map(int, input().split())
lst = []
dfs(0, 1)
