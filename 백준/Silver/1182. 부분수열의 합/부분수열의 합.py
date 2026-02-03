def dfs(n, s, sm, lst):
    global cnt
    # 정답 조건 먼저 확인 / 이후에 계속 가서 다른 조합 생길 수 있으니 return X !
    if lst and sm == S:
        cnt += 1

    # 끝까지 갔을 경우
    if n == N:
        return

    for i in range(s, N):
        dfs(n + 1, i + 1, sm + nums[i], lst + [nums[i]])


N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

dfs(0, 0, 0, [])  # S가 0인 경우를 확인 하기 위한 배열
print(cnt)