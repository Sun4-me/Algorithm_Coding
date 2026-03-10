import sys

def solve():
    # 빠른 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    dice = tuple(map(int, input_data))
    
    # 노드별 점수 하드코딩 (0~32번 노드)
    # 0: 시작, 1~20: 붉은색 외곽 경로, 21: 도착점
    # 22~24: 10에서 시작하는 파란색 경로 (13, 16, 19)
    # 25~26: 20에서 시작하는 파란색 경로 (22, 24)
    # 27~29: 30에서 시작하는 파란색 경로 (28, 27, 26)
    # 30~32: 중앙 교차점 이후 경로 (25, 30, 35)
    SCORES = (0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35)
    
    # 노드별 기본 다음 이동 위치
    ADJ = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 21, 23, 24, 30, 26, 30, 28, 29, 30, 31, 32, 20)
    
    # DEST[node][roll]: node에서 주사위 roll이 나왔을 때의 최종 도착 노드 사전 계산
    dest_temp = [[0] * 6 for _ in range(33)]
    for i in range(33):
        for r in range(1, 6):
            curr = i
            for step in range(r):
                # 이동 첫 걸음이고, 파란색 노드(5, 10, 15번)에서 시작했다면 파란색 경로로 진입
                if step == 0:
                    if curr == 5: curr = 22
                    elif curr == 10: curr = 25
                    elif curr == 15: curr = 27
                    else: curr = ADJ[curr]
                else:
                    curr = ADJ[curr]
            dest_temp[i][r] = curr
    
    # 접근 속도 향상을 위해 튜플로 변환
    DEST = tuple(tuple(row) for row in dest_temp)
    
    # 상태를 리스트 대신 인자로 풀어 전달 (p0, p1, p2, p3)
    def dfs(turn, current_score, v_mask, p0, p1, p2, p3):
        if turn == 10:
            return current_score
        
        roll = dice[turn]
        res = current_score
        
        # 1번 말(p0) 이동
        if p0 != 21:
            nxt = DEST[p0][roll]
            # 도착점이거나(21), 이동하려는 곳에 다른 말이 없다면(비트마스크 확인)
            if nxt == 21 or not (v_mask & (1 << nxt)):
                n_mask = v_mask
                if p0 != 0: n_mask &= ~(1 << p0)  # 기존 위치 비트 해제
                if nxt != 21: n_mask |= (1 << nxt) # 새 위치 비트 설정
                r = dfs(turn + 1, current_score + SCORES[nxt], n_mask, nxt, p1, p2, p3)
                if r > res: res = r
        
        # 2번 말(p1) 이동: 앞선 말이 시작점(0)을 떠났을 때만 이동 (중복 상태 제거)
        if p1 != 21 and p1 != p0:
            nxt = DEST[p1][roll]
            if nxt == 21 or not (v_mask & (1 << nxt)):
                n_mask = v_mask
                if p1 != 0: n_mask &= ~(1 << p1)
                if nxt != 21: n_mask |= (1 << nxt)
                r = dfs(turn + 1, current_score + SCORES[nxt], n_mask, p0, nxt, p2, p3)
                if r > res: res = r
                
        # 3번 말(p2) 이동
        if p2 != 21 and p2 != p0 and p2 != p1:
            nxt = DEST[p2][roll]
            if nxt == 21 or not (v_mask & (1 << nxt)):
                n_mask = v_mask
                if p2 != 0: n_mask &= ~(1 << p2)
                if nxt != 21: n_mask |= (1 << nxt)
                r = dfs(turn + 1, current_score + SCORES[nxt], n_mask, p0, p1, nxt, p3)
                if r > res: res = r
                
        # 4번 말(p3) 이동
        if p3 != 21 and p3 != p0 and p3 != p1 and p3 != p2:
            nxt = DEST[p3][roll]
            if nxt == 21 or not (v_mask & (1 << nxt)):
                n_mask = v_mask
                if p3 != 0: n_mask &= ~(1 << p3)
                if nxt != 21: n_mask |= (1 << nxt)
                r = dfs(turn + 1, current_score + SCORES[nxt], n_mask, p0, p1, p2, nxt)
                if r > res: res = r
                
        return res

    # 턴, 현재 점수, 방문 비트마스크, 말 4개의 초기 위치(0)
    print(dfs(0, 0, 0, 0, 0, 0, 0))

if __name__ == '__main__':
    solve()