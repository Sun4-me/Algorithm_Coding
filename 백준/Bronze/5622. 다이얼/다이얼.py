s = input()

li = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

cnt = 0

for i in range(len(s)):
    for j in li:
        if s[i] in j:
            cnt += li.index(j) + 3
print(cnt)
