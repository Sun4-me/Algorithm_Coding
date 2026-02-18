s = input()
target = input()

length = len(target)
stack = []

for i in s:
    stack.append(i)
    if ''.join(stack[-length:]) == target:
        for j in range(length):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
