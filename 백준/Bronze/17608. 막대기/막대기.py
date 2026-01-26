n = int(input())
stack = [int(input()) for _ in range(n)]

max_h = 0  # 가장 높은 건물
can_see = 0  # 볼 수 있는 건물

for _ in range(n):
    if max_h < stack[-1]:
        max_h = stack.pop()  # 높이 업데이트
        can_see += 1

    else:
        stack.pop()

print(can_see)
