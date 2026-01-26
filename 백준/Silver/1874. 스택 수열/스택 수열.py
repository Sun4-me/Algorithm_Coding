# 스택에 푸쉬할때는 오름차순으로 넣고 뺴서 수열 만듬
# 만들 수 있는가 없는가
# 만들 수 있다면 어떤 순서로

n = int(input())
nums = [int(input()) for _ in range(n)]
nums = nums[::-1]
stack = []
c_num = 0  # 어디까지 스택에 넣어놨는가
res = ""  # 목표로 하는 수열 갱신

ans = []

flag = True  # 가능한가

while True:
    if not nums:
        break

    if c_num <= nums[-1]:
        for i in range(c_num + 1, nums[-1]):
            stack.append(i)
            ans.append("+")

        c_num = nums[-1]
        res += str(nums.pop())
        ans.append("+")
        ans.append("-")


    else:
        if stack[-1] == nums[-1]:
            nums.pop()
            res += str(stack.pop())
            ans.append("-")
        else:
            flag = False
            break

if not flag:
    print("NO")
else:
    for i in ans:
        print(i)
