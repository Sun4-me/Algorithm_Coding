t = int(input())

for _ in range(t):
    word = input().split()
    for i in word:
        print(i[::-1], end=" ")
    print()
