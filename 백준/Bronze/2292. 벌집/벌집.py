n = int(input())
s = 1
cnt = 0
i = 1
while True:
    if s < n:
        s+=6*i
        cnt+=1
        i+=1
    else:
        break

print(cnt + 1)