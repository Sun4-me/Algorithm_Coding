n = int(input())
words = {input() for _ in range(n)}

res = sorted(words, key=lambda x: (len(x), x))

print(*res, sep='\n')
