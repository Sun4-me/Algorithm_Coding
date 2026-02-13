# from pprint import *


t = int(input())
for case in range(1, t + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    ans = 0

    for i in range(n):
        now_num = a[i]
        start = 0
        end = m - 1

        while start < end:
            middle = (start + end) // 2
            m_num = b[middle]

            if m_num < now_num:
                start = middle + 1

            elif m_num >= now_num:
                end = middle - 1

        if end > 0:
            if now_num > b[end]:
                ans += end + 1
            else:
                ans += end

        elif end == 0 and now_num > b[0]:
            ans += 1

    print(ans)
