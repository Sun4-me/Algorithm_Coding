from collections import deque
import sys

input = sys.stdin.readline
# 왼위아 왼위위 오위위 오위아 왼아위 왼아아 우아아 우아위
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]


def bfs(s, e):
    # 초기값 세팅
    visited = [[0] * n for _ in range(n)]
    visited[s[0]][s[1]] = 1
    q = deque([s])

    while q:
        cur = q.popleft()
        
        # 종료 체크를 다음 노드 찾기 전에 하자
        if cur == e:
            return visited[e[0]][e[1]] - 1
        
        for direct in range(8):
            ny = cur[0] + dy[direct]
            nx = cur[1] + dx[direct]
            if 0 <= ny <= n - 1 and 0 <= nx <= n - 1:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = visited[cur[0]][cur[1]] + 1
                    q.append((ny, nx))

    # 내가 잘 코드를 과연 잘 짯는가
    return "화이팅.."


t = int(input().rstrip())
for case in range(t):
    n = int(input())
    # 나이트 현재 위치
    cy, cx = map(int, input().split())
    # 나이트 목표 위치
    ey, ex = map(int, input().split())

    start = (cy, cx)
    end = (ey, ex)

    res = bfs(start, end)
    print(res)
