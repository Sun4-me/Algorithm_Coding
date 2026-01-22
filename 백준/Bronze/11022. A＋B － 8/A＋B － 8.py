import sys

input = sys.stdin.readline
t = int(input())

for case in range(t):
    a, b = map(int, input().split())
    print(f"Case #{case + 1}: {a} + {b} = {a + b}")
