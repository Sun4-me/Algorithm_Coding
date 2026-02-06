# 가능한 한 최대의 총 예산 배정
# 모든 요청이 배정 가능하면 그대로 배정
# 불가능하다면.. 특정한 정수 상한액 계산하고 그 이상인 예산요청에만 상한액 배정
# 상한액 이하는 요청한 금액 그대로 배정
# 지방의 수
n = int(input())
order = list(map(int, input().split()))
# 총 예산
m = int(input())
# 최대 배정 금액
ans = 0


def check(d):
    global m
    sm = 0
    for i in order:
        if i > d:
            sm += d
        else:
            sm += i

    if sm <= m:
        return True

    return False


def binary_search():
    global ans
    s, e = 0, max(order)

    while s <= e:
        m = (s + e) // 2
        if check(m):
            ans = m
            s = m + 1
        else:
            e = m - 1


binary_search()
print(ans)
