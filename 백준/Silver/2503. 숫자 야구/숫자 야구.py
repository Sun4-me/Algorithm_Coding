import sys

input = sys.stdin.readline

# 문제를 잘 읽어라
# 문제를 잘 읽어라
# 문제를 잘 읽어라
# 문제를 잘 읽어라
# 문제를 잘 읽어라
# 문제를 잘 읽어라
# 문제를 잘 읽어라
# 문제를 잘 읽어라
# 문제를 잘 읽어라
# 문제를 잘 읽어라
# 문제를 잘 읽어라



def check(a_num, b_num, strk, ball):
    s, b = 0, 0
    a_num = str(a_num)
    b_num = str(b_num)

    for k in range(3):
        if a_num[k] == b_num[k]:
            s += 1

        elif a_num[k] in b_num:
            b += 1

    if (s, b) == (strk, ball):
        return True

    else:
        return False


n = int(input())
log = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(102, 988):
    # 1부터 9사이다.. 문제를 잘 읽어라
    # 1부터 9사이다.. 문제를 잘 읽어라
    # 1부터 9사이다.. 문제를 잘 읽어라
    # 1부터 9사이다.. 문제를 잘 읽어라
    # 1부터 9사이다.. 문제를 잘 읽어라
    # 1부터 9사이다.. 문제를 잘 읽어라
    if len(set(str(i))) == 3 and not '0' in str(i):
        for j in log:
            if not check(i, j[0], j[1], j[2]):
                break
        else:
            cnt += 1

print(cnt)
