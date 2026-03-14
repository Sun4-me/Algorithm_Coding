import sys

sys.setrecursionlimit(100500)
input = sys.stdin.readline


def dfs(x):
    if v[x]:
        return

    v[x] = True
    real_ans.append(x)

    for nxt in adj[x]:
        if not v[nxt]:
            dfs(nxt)


############################################
N = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    # 양방향 그래프 처리
    adj[a].append(b)
    adj[b].append(a)

user_ans = list(map(int, input().split()))
############################################

# 시작점이 1이 아니라면 무조건 오답
if user_ans[0] != 1:
    print(0)
    sys.exit()

# 유저가 입력한 방문 순서를 기준으로 우선순위 배열 생성
order = [0] * (N + 1)
for i in range(N):
    order[user_ans[i]] = i

# 인접 리스트를 유저의 방문 순서에 맞춰 정렬
for i in range(1, N + 1):
    adj[i].sort(key=lambda x: order[x])

############################################
v = [False] * (N + 1)
real_ans = []
dfs(1)
############################################

res = 1 if user_ans == real_ans else 0
print(res)