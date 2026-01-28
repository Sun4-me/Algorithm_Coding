from collections import deque
import sys

input = sys.stdin.readline


###################
# 너비 우선 탐색 구현
def bfs(s, e):
    visited = [0] * (n + 1)
    visited[s] = 1
    q = deque([s])

    while q:
        curr = q.popleft()

        if curr == e:
            # 시작점 제외
            return visited[curr] - 1

        for nxt in adj[curr]:
            if visited[nxt] == 0:
                # 최단 경로 찾는거니까
                visited[nxt] = visited[curr] + 1
                q.append(nxt)

    return -1


# n: 도시의 개수, m: 도로의 개수
# 수도는 1번
###################
# input
n, m = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(m)]
q = int(input().rstrip())
cities = [list(map(int, input().split())) for _ in range(q)]
###################
# 인접 행렬 생성
adj = [[] for _ in range(n + 1)]
for row in nodes:
    adj[row[0]].append(row[1])
    adj[row[1]].append(row[0])
###################
# main
ans = []
for i in range(q):
    # 도로 정비할 때마다..
    adj[cities[i][0]].append(cities[i][1])
    adj[cities[i][1]].append(cities[i][0])
    # 각 도시별로 수도를 방문하는데 최소 방문 도시
    # 출력의 한줄 = row
    row = []
    for j in range(1, n + 1):
        row.append(bfs(1, j))

    ans.append(row)

for row in ans:
    print(*row)
