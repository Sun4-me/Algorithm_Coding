def dfs(depth, start):
    if depth == 6:
        print(*lst)
        return

    for i in range(start, k):
        lst.append(s[i])
        dfs(depth + 1, i + 1)
        lst.pop()


while True:
    s = list(map(int, input().split()))
    k = s.pop(0)

    if k == 0:
        break

    lst = []
    dfs(0, 0)

    print()
