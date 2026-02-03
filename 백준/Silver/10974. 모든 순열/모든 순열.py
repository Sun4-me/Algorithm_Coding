def dfs(n, lst):
    if n == N + 1:
        print(*lst)
        return

    for i in range(1, N + 1):
        if v[i] == 0:
            v[i] = 1
            dfs(n + 1, lst + [i])
            v[i] = 0


# 한 순열에서 숫자 한번씩 쓰고 사전 순으로 해야 함 -> v 사용
N = int(input())
v = [0] * (N + 1)
dfs(1, [])
