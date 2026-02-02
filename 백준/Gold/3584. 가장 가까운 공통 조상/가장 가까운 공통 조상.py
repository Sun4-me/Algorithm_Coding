import sys

sys.setrecursionlimit(10_010)


def recur(n, lst):
    # 루트인 경우 빈배열이니까 직접 넣어주자
    if n == root:
        lst.append(n)
        return

    lst.append(n)
    recur(adj[n], lst)


#################################################################
# 가장 가까운 공통 조상 찾자
# 두 노드에서 가장 가까운 것 즉 깊이가 가장 깊은 노드가 공통 조상임
t = int(input())
for case in range(t):
    # 노드의 수
    N = int(input())
    # 자식 -> 부모 정보를 나타내는 배열
    adj = [0] * (N + 1)
    for _ in range(N - 1):
        A, B = map(int, input().split())
        # 인덱스는 자식 안에있는건 부모, 빈 배열의 인덱스(부모가 없음)는 루트 노드
        adj[B] = A

    for i in range(1, N + 1):
        if adj[i] == 0:
            root = i

    # 공통 조상을 구할 두 노드
    target_a, target_b = map(int, input().split())

    v = [0] * (N + 1)
    #################################################################
    res_a = []
    res_b = []
    recur(target_a, res_a)
    recur(target_b, res_b)
    #################################################################
    find = False
    for i in range(len(res_a)):
        for j in range(len(res_b)):
            if res_a[i] == res_b[j]:
                find = True
                print(res_a[i])
                break
        # 찾았을 경우
        if find:
            break
