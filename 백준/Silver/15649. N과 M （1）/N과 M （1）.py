def dfs(n, lst):
    if n == M + 1:  # M개 고르기
        print(*lst)
        return

    for i in range(1, N + 1):  # 1부터 N까지의 자연수
        if v[i] == 0:
            v[i] = 1  # 방문 체크
            dfs(n + 1, lst + [i])  # 방문 체크한거 들고 가서 방문 안한 곳만 방문하게 됨
            v[i] = 0  # 다른 조합도 찾아야하니 방문 해제


# N까지 중복없이 M개 고르기
N, M = map(int, input().split())

# 중복 없이 하게 하기 위해 Visted 배열 이용
v = [0] * (N + 1)

# 1 부터시작, 빈리스트 제공
dfs(1, [])
