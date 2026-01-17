n = int(input())

cnt = 0

for _ in range(n):
    word = input()
    word_list = list(set(word))
    flag = True
    for i in word_list:
        if word.count(i) > 1:
            first = word.index(i)
            last = word.rindex(i)
            if word[first : last + 1].count(i) != last - first + 1:
                flag = False

    if flag:
        cnt += 1

print(cnt)
