from collections import deque
import sys

input = sys.stdin.readline


################################################
def bfs(s, e):
    node = (s, 1)
    q = deque([node])

    while q:
        cur_num, cur_dist = q.popleft()

        if cur_num == e:
            return cur_dist

        # 굳이 visited 만들 필요없음 거리까지 큐에 넣어서 해보자
        for nxt_num, nxt_dist in ((cur_num * 2, 0), (int(str(cur_num) + "1"), 0)):
            if nxt_num <= e:
                if nxt_dist == 0:
                    nxt_dist = cur_dist + 1
                    q.append((nxt_num, nxt_dist))

    return -1


################################################
a, b = map(int, input().split())
################################################
res = bfs(a, b)
################################################
print(res)
