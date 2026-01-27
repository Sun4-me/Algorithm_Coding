L = int(input())
M = 1234567891
r = 31
s = input()

answer = 0

for i in range(len(s)):
    num = ord(s[i]) - 96
    answer += num * (r ** i)

print(answer % M)
