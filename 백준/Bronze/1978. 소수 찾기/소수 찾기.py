n = int(input())
nums = list(map(int, input().split()))

def decimal(k):
    if k == 1:
        return False
    for i in range (k-1, 1, -1):
        if k % i == 0:
            return False
        else:
            continue
    return True


cnt = 0

for i in nums:
    if decimal(i):
        cnt += 1

print(cnt)
