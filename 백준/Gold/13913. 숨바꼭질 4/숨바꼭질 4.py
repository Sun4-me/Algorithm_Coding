import sys
from collections import deque



def bfs():
    global n, k
    v = [0] * 100001
    p = [-1] * 100001
    v[n] = 1

    q = deque([n])

    while q:
        curr = q.popleft()

        if v[k] != 0 and v[curr] > v[k]:
            continue

        if curr == k:
            print(v[curr] - 1)

            ans = []
            temp = k
            while temp != -1:
                ans.append(temp)
                temp = p[temp]

            print(*ans[::-1])
            sys.exit()

        for nxt in (curr * 2, curr - 1, curr + 1):
            if 0 <= nxt <= 100000:
                if v[nxt] == 0:
                    v[nxt] = v[curr] + 1
                    p[nxt] = curr
                    q.append(nxt)


n, k = map(int, input().split())
bfs()
