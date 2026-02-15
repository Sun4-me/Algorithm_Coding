def dfs(depth, s):
    if depth == m:
        print(*lst)
        return

    used = 0

    for i in range(s, n):
        if nums[i] != used:
            lst.append(nums[i])
            used = nums[i]
            dfs(depth + 1, i+1)
            lst.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

lst = []
dfs(0, 0)
