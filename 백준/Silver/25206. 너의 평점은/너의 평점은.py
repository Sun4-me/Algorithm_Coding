ranked_dict = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0, }

jihoon = [input().split()[1:] for _ in range(20)]

total = 0  # 학점의 총합
score = 0  # 학점 x 과목 평점

for i in range(20):
    if jihoon[i][1] != "P":
        total += float(jihoon[i][0])
        score += float(jihoon[i][0]) * float(ranked_dict[jihoon[i][1]])

print(score / total)
