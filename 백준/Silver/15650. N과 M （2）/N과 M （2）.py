def dfs(n, s, lst):
    # 종료 조건 처리 + 정답 처리
    if n == M:  # M개의 수열 완성
        ans.append(lst)
        return

    # 하부 함수 호출
    for i in range(s, N + 1):
        dfs(n + 1, i + 1, lst + [i])


N, M = map(int, input().split())
ans = []

dfs(0, 1, [])
for lst in ans:
    print(*lst)
