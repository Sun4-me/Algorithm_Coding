n = int(input())
nums = list(map(int, input().split()))
ans = [0] * n
stack = []

for i in range(n - 1, -1, -1):
    while stack and nums[i] > nums[stack[-1]]:
        idx = stack.pop()
        ans[idx] = i + 1
    stack.append(i)

print(*ans)
