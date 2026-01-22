# L미터 케이크  방청객 N명에게 케이크
# 조각: 1미터 단위 1 ~ l
# 방척객: 1 ~ N 번호
# 방청객은 P부터 K까지 조각을 원해함
# 이미 번호가 있을 경우 PASS
# 가장 많은 케이크 조각을 받을 것으로 기대한 방청객의 번호
# 실제로 가장 많은 케이크 조각을 받는 방청객
import sys

input = sys.stdin.readline
L = int(input())
N = int(input())
nodes = [list(map(int, input().split())) for _ in range(N)]

expect = []
actual = [0] * (L + 1)

for row in nodes:
    expect.append(row[1] - row[0] + 1)

row_idx = 0
for row in nodes:
    row_idx += 1
    p, k = row[0], row[1]
    for i in range(p, k + 1):
        if actual[i] == 0:
            actual[i] = row_idx


expect_idx = 0
max_expect = max(expect)

for i in expect:
    expect_idx += 1
    if i == max_expect:
        break


actual_counts = []
for i in range(1, N + 1):
    actual_counts.append(actual.count(i))

actual_idx = 0
max_actual = max(actual_counts)

for i in actual_counts:
    actual_idx += 1
    if i == max_actual:
        break

print(expect_idx)
print(actual_idx)
