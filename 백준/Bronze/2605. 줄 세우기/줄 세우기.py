# 첫번째 줄 을 서면 무조건 0번받고 맨 앞
# 두번째는 0또는 1 중 하나
# -> 0일 경우 그자리에 그대로
# -> 1일 경우 앞 학생 앞으로
# 세번째는 0, 1, 2
# 뽑은 번호만큼 앞자리로 가서 줄
# 각자 뽑은 번호는 자신이 처음에 선 순서보다는 작은 수이다.
n = int(input())
nums = list(map(int, input().split()))
student = [i for i in range(1, n + 1)]
res = []

while student:
    curr_n = nums.pop(0)
    curr_s = student.pop(0)

    res.insert(curr_n, curr_s)

res = res[::-1]
print(*res)
