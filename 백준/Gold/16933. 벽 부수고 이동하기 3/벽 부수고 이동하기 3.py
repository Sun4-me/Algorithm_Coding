from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    v = [[-1] * M for _ in range(N)]
    v[0][0] = K
    q = deque([(0, 0, K, 1)])

    while q:
        cy, cx, k, dist = q.popleft()

        if cy == N - 1 and cx == M - 1:
            return dist

        # 거리가 홀수면 낮, 짝수면 밤으로 판단
        is_day = (dist % 2 != 0)

        # 사방이 벽일 때 밤이어서 큐에 대기 상태가 중복으로 4번 들어가는 것을 막는 플래그
        wait_added = False

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < M:
                # 1. 이동할 곳이 빈 칸('0')인 경우
                if grid[ny][nx] == 0:
                    # 이전에 여기 온 경로보다 남은 파워(K)가 클 때만 갱신 후 이동
                    if v[ny][nx] < k:
                        v[ny][nx] = k
                        q.append((ny, nx, k, dist + 1))

                # 2. 이동할 곳이 벽('1')인 경우
                # 벽을 뚫을 힘이 있고, 벽 너머의 칸을 지금보다 더 많은 파워로 방문한 적이 없을 때만
                elif k > 0 and v[ny][nx] < k - 1:
                    if is_day:
                        # 낮이면 벽을 부수고 전진
                        v[ny][nx] = k - 1
                        q.append((ny, nx, k - 1, dist + 1))
                    else:
                        # 밤이면 부술 수 없으니 현재 자리에서 하루 대기 (거리만 +1)
                        if not wait_added:
                            q.append((cy, cx, k, dist + 1))
                            wait_added = True

    return -1


########################################################
N, M, K = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
########################################################
print(bfs())
