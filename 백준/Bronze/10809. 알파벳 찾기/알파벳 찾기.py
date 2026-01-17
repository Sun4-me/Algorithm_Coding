s = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
    if i not in s:
        print(-1, end=" ")
    else:
        print(s.index(i), end=" ")
