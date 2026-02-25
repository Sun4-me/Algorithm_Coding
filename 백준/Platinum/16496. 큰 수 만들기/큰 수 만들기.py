n = int(input())
nums = list(input().split())

nums.sort(key=lambda x: x * 10, reverse=True)

res = ''.join(nums)

if res[0] == '0':
    print(0)
else:
    print(res)
