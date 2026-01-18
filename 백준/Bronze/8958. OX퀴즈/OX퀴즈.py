t = int(input())

for _ in range(t):
    temp = input()
    score = 0
    res = 0
    for i in range(len(temp)):
        if temp[i] == "O":
            score += 1
            res += score
        else:
            score = 0
    print(res)
