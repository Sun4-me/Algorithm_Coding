# 2n 직사각형까지 몇번의 방법이 있는지 저장해두기
n = int(input())

dp = [0] * (1001)
dp[1] = 1
dp[2] = 3
dp[3] = 5
dp[4] = 11
dp[5] = 21

# 5까지 그리니까 점화식을 유레카..
for i in range(6, n + 1):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]

print(dp[n] % 10007)
