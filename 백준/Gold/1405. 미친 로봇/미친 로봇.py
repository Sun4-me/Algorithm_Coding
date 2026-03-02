def dfs(depth, y, x, per):
    global ans
    if per == 0:
        return

    if depth == N:
        ans += per
        return

    for dy, dx, go_per in ((-1, 0, n), (1, 0, s), (0, -1, w), (0, 1, e)):
        if (y + dy, x + dx) not in st:
            st.add((y + dy, x + dx))
            dfs(depth + 1, y + dy, x + dx, per * (go_per / 100))  # 동
            st.remove((y + dy, x + dx))


N, e, w, s, n = map(int, input().split())
st = set()
st.add((0, 0))
ans = 0

dfs(0, 0, 0, 1)

print(ans)
