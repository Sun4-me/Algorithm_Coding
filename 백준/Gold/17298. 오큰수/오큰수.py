n = int(input())
nums = list(map(int, input().split()))
ans = [0] * n
stack = []

for i in range(n - 1, -1, -1):
    while stack and nums[i] >= stack[-1]:
        stack.pop()
    if stack:
        ans[i] = stack[-1]
    else:
        ans[i] = -1

    stack.append(nums[i])

print(*ans)
