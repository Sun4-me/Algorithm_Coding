# 나무 M, 높이 H
# M 미터만 가져갈 높이의 최댓값 구하기
n, m = map(int, input().split())
trees = list(map(int, input().split()))
ans = 0


def check(h):
    global m
    sm = 0
    for i in trees:
        if i > h:
            sm += (i - h)
    if sm >= m:
        return True
    return False


def binary_search():
    global ans
    s, e = 0, max(trees)

    while s <= e:
        m = (s + e) // 2
        if check(m):
            ans = m
            s = m + 1
        else:
            e = m - 1


binary_search()
print(ans)
