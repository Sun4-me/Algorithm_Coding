def cal(lst):
    sum = 0
    for i in range(len(lst) - 1):
        sum += abs(lst[i] - lst[i + 1])
    return sum


def dfs(depth, lst):
    global res
    if depth == N + 1:
        res = max(res, cal(lst))
        return

    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(depth + 1, lst + [nums[i]])
            v[i] = 0


N = int(input())
nums = list(map(int, input().split()))
v = [0] * N
res = 0

dfs(1, [])
print(res)
