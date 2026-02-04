# 팀 시너지를 구해주는 함수
def cal(lst):
    res = 0
    # 모든 쌍을 구해야 함
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            p1 = lst[i]
            p2 = lst[j]
            res += synergy[p1][p2] + synergy[p2][p1]

    return res


def dfs(depth, s, lst):
    global min_num
    # 가지치기
    # 첫 시작이 아닌 경우, 0번을 포함한 경우를 다세면 반을 센거임.
    # 굳이 다셀 필요 없음 반만 세고 나머지는 set으로 반 찾자.
    # 근데 이게 더 빠를까...?
    # 처음에 이거 생각했는데 생각해보니까 그냥 밑에 for문에서 가지쳐버리면 됨
    # if depth != 0 and lst[0] != 0:
    #     return


    if depth == n // 2:
        people = set([i for i in range(n)])  # 매번 이렇게 해야 하긴 하는데 뭐가 더 빠를까..
        for i in lst:
            people.remove(i)  # 반대편 팀을 만들기 위해 우리 팀을 뺌
        min_num = min(min_num, abs(cal(lst) - cal(list(people))))
        return

    # 순서가 중요한게 아니니까
    for i in range(s, n):
        # 여기서 그냥 아싸리 안뽑는게 나을듯 이러면 위에 가지치기가 필요 없음
        if depth == 0 and i > 0:
            return

        dfs(depth + 1, i + 1, lst + [i])


# 축구를 하기 위해 모인 사람은 총 N명, N은 짝수
# N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나누자
n = int(input())
synergy = [list(map(int, input().split())) for _ in range(n)]

min_num = 10 ** 8
dfs(0, 0, [])

print(min_num)
