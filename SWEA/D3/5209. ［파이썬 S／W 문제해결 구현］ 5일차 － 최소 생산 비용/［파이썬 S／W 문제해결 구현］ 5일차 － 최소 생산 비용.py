def dfs(n, sm):
    global res
    # 커지는 경우 더 탐색할 필요 없음
    if sm >= res:
        return

    if n == N:
        # 최소 값일 경우
        res = min(res, sm)
        return

    for x in range(N):
        if v[x] == 0:
            v[x] = 1
            dfs(n + 1, sm + grid[n][x])
            v[x] = 0


t = int(input())
for case in range(t):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    # x의 인덱스 중복 방지
    v = [0] * N
    # 최소 생산 비용
    res = 100 * 3
    # 0번, 합0
    dfs(0, 0)
    print(f"#{case + 1} {res}")
