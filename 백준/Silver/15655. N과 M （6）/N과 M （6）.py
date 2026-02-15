def dfs(depth, s):
    if depth == m:
        print(*lst)
        return

    for i in range(s, n):
        lst.append(nums[i])
        dfs(depth + 1, i + 1)
        lst.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

v = [0] * n

lst = []
dfs(0, 0)
