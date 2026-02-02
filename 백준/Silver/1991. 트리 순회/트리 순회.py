# 전위
def pre_ord(n):
    global pre_res
    pre_res += n
    if n in left_child.keys():
        pre_ord(left_child[n])
    if n in right_child.keys():
        pre_ord(right_child[n])


# 중위
def in_ord(n):
    global in_res
    if n in left_child.keys():
        in_ord(left_child[n])
    in_res += n
    if n in right_child.keys():
        in_ord(right_child[n])


# 후위
def post_ord(n):
    global post_res
    if n in left_child.keys():
        post_ord(left_child[n])
    if n in right_child.keys():
        post_ord(right_child[n])
    post_res += n


############################################
# 노드의 개수
N = int(input())
# 문자니까 딕셔너리로 관리하자
left_child = dict()
right_child = dict()
for _ in range(N):
    node, L, R = input().split()
    if L != '.':
        left_child[node] = L  # 이진이니까 딕셔너리 초기화만 하면 됨

    if R != '.':
        right_child[node] = R
############################################
pre_res = ""
in_res = ""
post_res = ""
pre_ord("A")
in_ord("A")
post_ord("A")
############################################
print(pre_res)
print(in_res)
print(post_res)
