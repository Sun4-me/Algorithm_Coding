import sys

input = sys.stdin.readline

N = int(input())
count = [0] * 10001

for _ in range(N):
    num = int(input())
    count[num] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)