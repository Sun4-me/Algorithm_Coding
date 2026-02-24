s = input().split('-')
total = 0

for i in range(len(s)):
    if i == 0:
        if '+' in s[i]:
            temp = s[i].split('+')
            for j in temp:
                total += int(j)

        else:
            total += int(s[i])

    else:
        if '+' in s[i]:
            temp = s[i].split('+')
            now_sum = 0
            for j in temp:
                now_sum += int(j)

            total -= now_sum

        else:
            total -= int(s[i])

print(total)
