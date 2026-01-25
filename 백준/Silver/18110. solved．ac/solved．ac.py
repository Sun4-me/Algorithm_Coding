import sys

input = sys.stdin.readline

n = int(input())
lst = sorted([int(input()) for _ in range(n)])

if n == 0:
    print(0)

else:
    exclude_cnt = int(n * 0.15 + 0.5)
    lst = lst[exclude_cnt: n - exclude_cnt]
    ans = int(sum(lst) / (n - 2 * exclude_cnt) + 0.5)
    print(ans)
