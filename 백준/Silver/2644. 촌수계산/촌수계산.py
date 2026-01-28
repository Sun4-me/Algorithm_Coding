from collections import deque
import sys

input = sys.stdin.readline


def bfs(s, e):
    # 초기 세팅
    visited = [0] * (n + 1)
    visited[s] = 1
    step = 1
    q = deque([s])

    while q:
        # 스탭바이 스탭용 범위만 담는 큐
        nq = deque()

        ##### q 에 있는 것을 다 털어야 하는데 안털어서 틀렸었음 #####
        for cur in q:
            for nxt in adj[cur]:
                if nxt == e:
                    return step

                elif visited[nxt] == 0:
                    visited[nxt] = 1
                    nq.append(nxt)

        q = nq
        step += 1

    return -1


# 전체 사람 수
n = int(input().rstrip())
start, end = map(int, input().split())
# 부모 자식들 간 관계의 개수
m = int(input().rstrip())
# x는 y의 부모 번호
nodes = [list(map(int, input().split())) for _ in range(m)]

# 인접 행렬 생성
adj = [[] for _ in range(n + 1)]
for row in nodes:
    adj[row[0]].append(row[1])
    adj[row[1]].append(row[0])

res = bfs(start, end)
print(res)
