from itertools import combinations

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

start = 1  # 최소거리
end = houses[-1] - houses[0]  # 최대거리
ans = 0

while start <= end:
    mid = (start + end) // 2

    count = 1
    current = houses[0]

    for i in range(1, n):
        if houses[i] - current >= mid:
            count += 1
            current = houses[i]

    if count >= c:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
