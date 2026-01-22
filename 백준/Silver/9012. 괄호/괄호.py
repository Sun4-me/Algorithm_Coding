n = int(input())

for _ in range(n):
    test = input()
    stack = []

    flag = True

    for i in test:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                flag = False
                break

    if not flag or stack:
        print("NO")

    else:
        print("YES")