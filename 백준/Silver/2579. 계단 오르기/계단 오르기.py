import sys

n = int(input())
nums = [int(input()) for _ in range(n)]
# 한칸 출신, 두칸 출신
dp = [[0, 0] for _ in range(301)]

# WARNING #
############ 엣지 발생 위험 지역 처리 ############
if n == 1:
    print(nums[0])
    sys.exit()
###############################################


############ 한칸, 두칸
dp[0] = [nums[0], nums[0]]
dp[1] = [nums[1] + nums[0], nums[1]]

for i in range(2, n):
    # 한칸 출신이면 하나만 보고, 두칸 출신이면 한칸, 두칸 중에 큰거 보자
    dp[i] = [dp[i - 1][1] + nums[i], max(dp[i - 2][0] + nums[i], dp[i - 2][1] + nums[i])]

print(max(dp[n - 1]))
