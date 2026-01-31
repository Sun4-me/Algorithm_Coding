s = input()
stack = []

for i in s:
    if i == '(':
        stack.append('(')
    elif i == 'H':
        stack.append('1')
    elif i == 'C':
        stack.append('12')
    elif i == 'O':
        stack.append('16')
    elif i == ')':
        num = 0
        while True:
            tmp = stack.pop()
            if tmp == '(':
                break
            else:
                num += int(tmp)
        stack.append(num)
    else:
        num = int(stack.pop())
        stack.append(num * int(i))

ans = 0
for num in stack:
    ans += int(num)
print(ans)
