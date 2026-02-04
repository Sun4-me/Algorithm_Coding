def cal(a, b, oper):
    res = 0
    if oper == 0:
        res = a + b
    elif oper == 1:
        res = a - b
    elif oper == 2:
        res = a * b
    elif oper == 3:
        if a < 0 and b > 0:
            a = -a
            res = a // b
            res = -res
        else:
            res = a // b
    return res


def dfs(depth, sm):
    global min_num, max_num

    if depth == N - 1:
        min_num = min(min_num, sm)
        max_num = max(max_num, sm)
        return

    for i in range(4):
        if operator[i] != 0:
            operator[i] -= 1
            dfs(depth + 1, cal(sm, nums[depth + 1], i))
            operator[i] += 1


######################################################
N = int(input())
nums = list(map(int, input().split()))
# 이놈들의 합은 N-1
operator = list(map(int, input().split()))
min_num = 10 ** 11
max_num = - 10 ** 11
dfs(0, nums[0])

print(max_num)
print(min_num)
