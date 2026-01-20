s = int(input())
score = list(map(int, input().split()))

max_score = max(score)

for i in range(s):
    score[i] = score[i] / max_score * 100

average = sum(score) / s

print(average)
