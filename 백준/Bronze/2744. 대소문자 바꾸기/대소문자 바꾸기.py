word = input()
newword = ""
for i in word:
    if i.islower():
        newword += i.upper()
    else:
        newword += i.lower()

print(newword)