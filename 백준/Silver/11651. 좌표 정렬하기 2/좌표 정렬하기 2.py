n = int(input())
nodes = [list(map(int, input().split())) for _ in range(n)]
nodes.sort(key= lambda x : (x[1], x[0]))
for i in nodes:
    print(*i)
