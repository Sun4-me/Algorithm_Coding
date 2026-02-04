def dfs(depth, s, lst):
    global cnt

    if sum(lst) > R:
        return

    if len(lst) >= 2:
        if L <= sum(lst) and max(lst) - min(lst) >= X:
            cnt += 1

    for i in range(s, N):
        dfs(depth + 1, i + 1, lst + [difficult[i]])


# 문제 N개
# i번째 문제의 난이도는 Ai이다
# 두 문제 이상
# 난이도의 합은 L보다 크거나 같고, R보다 작거나 같아야 한다
# 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X보다 크거나 같아야 한다.
N, L, R, X = map(int, input().split())
difficult = list(map(int, input().split()))
cnt = 0
dfs(0, 0, [])
print(cnt)
