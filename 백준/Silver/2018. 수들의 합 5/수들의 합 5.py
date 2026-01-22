n = int(input())

count = 1  # 자기 자신
start = 1  # 왼쪽 끝
end = 1  # 오른쪽 끝
sum_nums = 1  # 현재 범위안 합

while end != n:
    if sum_nums == n:
        count += 1
        end += 1
        sum_nums += end

    elif sum_nums > n:
        sum_nums -= start
        start += 1

    else:
        end += 1
        sum_nums += end

print(count)
