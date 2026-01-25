# 문자열로 관리
room_num = input()

# 0부터 9까지 키값, 0 value로 설정
cnt_dict = {i: 0 for i in range(10)}

# 입력값에 따라 딕셔너리 업데이트
for i in room_num:
    cnt_dict[int(i)] += 1

# 6, 9 는 반올림 기법으로 재업데이트
six_nine = int((cnt_dict[6] + cnt_dict[9]) / 2 + 0.5)
cnt_dict[6] = six_nine
cnt_dict[9] = six_nine

# 가장 큰 value 가 세트의 수 이므로..
print(max(cnt_dict.values()))
