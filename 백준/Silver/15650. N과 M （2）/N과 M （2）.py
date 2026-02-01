def dfs(n, lst):
    # 종료 조건 처리 + 정답 처리
    if n == M:  # M개의 수열 완성

        for i in range(M - 1):
            if lst[i] >= lst[i + 1]:
                break
        else:
            ans.append(lst)
            return

    # 하부 함수 호출
    for i in range(1, N + 1):
        if v[i] == 0:
            v[i] = 1
            dfs(n + 1, lst + [i])
            v[i] = 0


N, M = map(int, input().split())
ans = []
v = [0] * (N + 1)

dfs(0, [])
for lst in ans:
    print(*lst)
