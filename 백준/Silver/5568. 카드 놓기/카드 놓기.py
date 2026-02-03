def dfs(depth, num):
    if num and depth == k:
        ans.add(num)

    if depth == n:
        return

    for i in range(n):
        if v[i] == 0:
            v[i] = 1
            dfs(depth + 1, num + cards[i])
            v[i] = 0


n = int(input())
k = int(input())
cards = [input() for _ in range(n)]

ans = set()  # 중복을 제거하자
v = [0] * (n + 1)  # 중복 선택을 방지하자
dfs(0, "")

print(len(ans))
