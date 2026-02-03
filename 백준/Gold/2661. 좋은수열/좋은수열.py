def dfs(depth, ans):
    if depth >= 2 and ans[depth - 2:depth - 1] == ans[depth - 1:depth]:
        return
    if depth >= 4 and ans[depth - 4:depth - 2] == ans[depth - 2:depth]:
        return
    if depth >= 6 and ans[depth - 6:depth - 3] == ans[depth - 3:depth]:
        return
    if depth >= 8 and ans[depth - 8:depth - 4] == ans[depth - 4:depth]:
        return
    if depth >= 10 and ans[depth - 10:depth - 5] == ans[depth - 5:depth]:
        return
    if depth >= 12 and ans[depth - 12:depth - 6] == ans[depth - 6:depth]:
        return
    if depth >= 14 and ans[depth - 14:depth - 7] == ans[depth - 7:depth]:
        return
    if depth >= 16 and ans[depth - 16:depth - 8] == ans[depth - 8:depth]:
        return
    if depth >= 18 and ans[depth - 18:depth - 9] == ans[depth - 9:depth]:
        return
    if depth >= 20 and ans[depth - 20:depth - 10] == ans[depth - 10:depth]:
        return
    if depth >= 22 and ans[depth - 22:depth - 11] == ans[depth - 11:depth]:
        return
    if depth >= 24 and ans[depth - 24:depth - 12] == ans[depth - 12:depth]:
        return
    if depth >= 26 and ans[depth - 26:depth - 13] == ans[depth - 13:depth]:
        return
    if depth >= 28 and ans[depth - 28:depth - 14] == ans[depth - 14:depth]:
        return
    if depth >= 30 and ans[depth - 30:depth - 15] == ans[depth - 15:depth]:
        return
    if depth >= 32 and ans[depth - 32:depth - 16] == ans[depth - 16:depth]:
        return
    if depth >= 34 and ans[depth - 34:depth - 17] == ans[depth - 17:depth]:
        return
    if depth >= 36 and ans[depth - 36:depth - 18] == ans[depth - 18:depth]:
        return
    if depth >= 38 and ans[depth - 38:depth - 19] == ans[depth - 19:depth]:
        return
    if depth >= 40 and ans[depth - 40:depth - 20] == ans[depth - 20:depth]:
        return
    if depth >= 42 and ans[depth - 42:depth - 21] == ans[depth - 21:depth]:
        return
    if depth >= 44 and ans[depth - 44:depth - 22] == ans[depth - 22:depth]:
        return
    if depth >= 46 and ans[depth - 46:depth - 23] == ans[depth - 23:depth]:
        return
    if depth >= 48 and ans[depth - 48:depth - 24] == ans[depth - 24:depth]:
        return
    if depth >= 50 and ans[depth - 50:depth - 25] == ans[depth - 25:depth]:
        return
    if depth >= 52 and ans[depth - 52:depth - 26] == ans[depth - 26:depth]:
        return
    if depth >= 54 and ans[depth - 54:depth - 27] == ans[depth - 27:depth]:
        return
    if depth >= 56 and ans[depth - 56:depth - 28] == ans[depth - 28:depth]:
        return
    if depth >= 58 and ans[depth - 58:depth - 29] == ans[depth - 29:depth]:
        return
    if depth >= 60 and ans[depth - 60:depth - 30] == ans[depth - 30:depth]:
        return
    if depth >= 62 and ans[depth - 62:depth - 31] == ans[depth - 31:depth]:
        return
    if depth >= 64 and ans[depth - 64:depth - 32] == ans[depth - 32:depth]:
        return
    if depth >= 66 and ans[depth - 66:depth - 33] == ans[depth - 33:depth]:
        return
    if depth >= 68 and ans[depth - 68:depth - 34] == ans[depth - 34:depth]:
        return
    if depth >= 70 and ans[depth - 70:depth - 35] == ans[depth - 35:depth]:
        return
    if depth >= 72 and ans[depth - 72:depth - 36] == ans[depth - 36:depth]:
        return
    if depth >= 74 and ans[depth - 74:depth - 37] == ans[depth - 37:depth]:
        return
    if depth >= 76 and ans[depth - 76:depth - 38] == ans[depth - 38:depth]:
        return
    if depth >= 78 and ans[depth - 78:depth - 39] == ans[depth - 39:depth]:
        return
    if depth >= 80 and ans[depth - 80:depth - 40] == ans[depth - 40:depth]:
        return

    # 정답일 경우
    if depth == n:
        print(ans)
        quit()
        return

    # 이 순서대로 탐색 보내면 맨 처음 찾은게 가장 작은게 아닐까?
    dfs(depth + 1, ans + "1")
    dfs(depth + 1, ans + "2")
    dfs(depth + 1, ans + "3")


# 백트래킹으로 풀 수 있어보이는데..
# n이 80이하? 강력한 가지치기가 필요해보인다..
# 인접한 1개, 2개, 3개만 확인하고 넘기면 됨
# 가장 작은 수만 출력하면 됨
n = int(input())
################
dfs(0, "")
