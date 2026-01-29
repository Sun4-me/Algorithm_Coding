from collections import deque


################################################
def bfs():
    visited = [0] * 10001
    start = a
    visited[start] = 1
    q = deque([start])

    while q:
        curr = q.popleft()

        if curr == b:
            return visited[curr] - 1

        ## 가능한 다음 후보를 계산하자, 플러스 마이너스 텀 다르게 사용 주의 ##
        nxt_list = []
        plus_term = 1
        minus_term = 1
        while True:
            if curr + bridge[curr] * plus_term <= n:
                nxt_list.append(curr + bridge[curr] * plus_term)
                plus_term += 1
            elif curr - bridge[curr] * minus_term >= 1:
                nxt_list.append(curr - bridge[curr] * minus_term)
                minus_term += 1
            else:
                break
        ##########################

        for nxt in nxt_list:
            if visited[nxt] == 0:
                visited[nxt] = visited[curr] + 1
                q.append(nxt)

    return -1


################################################
n = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())
################################################
# 인덱스 관리 편하게 0번째 하나 넣어주기
bridge.insert(0, 0)
################################################
res = bfs()
################################################
print(res)
