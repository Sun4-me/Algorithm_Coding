import sys

input = sys.stdin.readline
sys.setrecursionlimit(100300)


def dfs(x):
    global team_cnt

    v[x] = True
    nxt = nums[x]

    if not v[nxt]:
        dfs(nxt)

    elif not f[nxt]:
        curr = nxt
        while curr != x:
            team_cnt += 1
            curr = nums[curr]
        team_cnt += 1

    f[x] = True


t = int(input())
for case in range(t):
    n = int(input())
    nums = [0] + list(map(int, input().split()))

    v = [False] * (n + 1)
    f = [False] * (n + 1)
    team_cnt = 0

    for i in range(1, n + 1):
        if not v[i]:
            dfs(i)

    print(n - team_cnt)
