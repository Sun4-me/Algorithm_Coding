def dfs(depth):
    if depth == m:
        print(*lst)
        return

    used = 0

    for i in range(n):
        if v[i] == 0 and nums[i] != used:
            lst.append(nums[i])
            v[i] = 1
            used = nums[i]
            dfs(depth + 1)
            v[i] = 0
            lst.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

v = [0] * n

lst = []
dfs(0)
