from collections import deque


def bfs(s, e):
    v = [0] * 100_001
    v[s] = 1
    q = deque([s])
    
    cnt = 0
    time = 0

    while q:
        curr = q.popleft()

        if curr == e:
            if cnt == 0:
                time = v[curr]
            cnt += 1
            continue

        for nxt in (curr - 1, curr + 1, curr * 2):
            if 0 <= nxt <= 100000:
                if v[nxt] == 0 or v[nxt] == v[curr] + 1:
                    v[nxt] = v[curr] + 1
                    q.append(nxt)

    return time, cnt


# 수빈이 n, 동생 k
n, k = map(int, input().split())
time, cnt = bfs(n, k)
print(time - 1)
print(cnt)
