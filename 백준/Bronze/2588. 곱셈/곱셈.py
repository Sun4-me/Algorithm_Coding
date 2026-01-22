a = int(input())
b = int(input())

one = b % 10
ten = (b // 10) % 10
hund = b // 100

print(a * one)
print(a * ten)
print(a * hund)
print(a * b)
