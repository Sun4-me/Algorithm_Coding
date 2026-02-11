from collections import deque


def bfs():
    global n, k
    v = [0] * 100001
    v[n] = 1

    q = deque([n])

    cnt = 0
    time = 0

    while q:
        curr = q.popleft()

        if v[k]!= 0 and v[curr] > v[k]:
            continue

        if curr == k:
            if time == 0:
                time = v[curr]
            cnt += 1
            continue


        for nxt in (curr - 1, curr + 1, curr * 2):
            if 0 <= nxt <= 100000:
                if v[nxt] == 0 or v[nxt] == v[curr] + 1:
                    v[nxt] = v[curr] + 1
                    q.append(nxt)


    return cnt, time


n, k = map(int, input().split())
cnt, time = bfs()

print(time - 1)
print(cnt)
