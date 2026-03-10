import sys

def solve():
    # 빠른 입력
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    dice = tuple(map(int, input_data))

    # 읽기 전용 데이터는 모두 Tuple로 선언하여 속도 극대화
    SCORE = (
        0, 2, 4, 6, 8, 10,
        12, 14, 16, 18, 20,
        22, 24, 26, 28, 30,
        32, 34, 36, 38, 40,
        13, 16, 19,
        22, 24,
        28, 27, 26,
        25, 30, 35,
        0
    )

    nxt = (
        1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11,
        12, 13, 14, 15, 16,
        17, 18, 19, 20, 32,
        22, 23, 29,
        25, 29,
        27, 28, 29,
        30, 31, 20,
        32
    )

    blue = [0] * 33
    blue[5], blue[10], blue[15] = 21, 24, 26

    # 2차원 배열 대신 1차원 리스트로 메모리 할당 (크기: 33 * 6)
    MOVE_list = [0] * 198  
    for i in range(33):
        for d in range(1, 6):
            x = i
            step = d
            if x != 32:
                if blue[x]:
                    x = blue[x]
                    step -= 1
                else:
                    x = nxt[x]
                    step -= 1
                while step and x != 32:
                    x = nxt[x]
                    step -= 1
            # 2차원 인덱스를 1차원으로 변환 (i * 6 + d)
            MOVE_list[i * 6 + d] = x
            
    # 완성된 1차원 리스트를 Tuple로 고정하여 접근 속도 부스팅
    MOVE = tuple(MOVE_list)

    ans = 0

    # 상태를 리스트 대신 4개의 로컬 변수(p0, p1, p2, p3)로 언롤링
    def dfs(depth, total, p0, p1, p2, p3):
        nonlocal ans # 전역 변수 대신 nonlocal 사용으로 스코프 탐색 최적화
        
        # 적용하신 완벽한 A* 휴리스틱 가지치기
        if total + 40 * (10 - depth) <= ans:
            return
            
        if depth == 10:
            # 가지치기를 통과하여 여기까지 왔다면 무조건 total > ans 임이 보장됨
            # max() 함수 호출 생략
            ans = total 
            return
            
        d = dice[depth]
        
        # 0번 말 이동
        if p0 != 32:
            nx = MOVE[p0 * 6 + d]
            # 도착했거나, 다른 말이 그 자리에 없는 경우
            if nx == 32 or (nx != p1 and nx != p2 and nx != p3):
                dfs(depth + 1, total + SCORE[nx], nx, p1, p2, p3)
                
        # 1번 말 이동 (대칭성 제거: p1 != p0)
        if p1 != 32 and p1 != p0:
            nx = MOVE[p1 * 6 + d]
            if nx == 32 or (nx != p0 and nx != p2 and nx != p3):
                dfs(depth + 1, total + SCORE[nx], p0, nx, p2, p3)
                
        # 2번 말 이동 (대칭성 제거: p2 != p0 and p2 != p1)
        if p2 != 32 and p2 != p0 and p2 != p1:
            nx = MOVE[p2 * 6 + d]
            if nx == 32 or (nx != p0 and nx != p1 and nx != p3):
                dfs(depth + 1, total + SCORE[nx], p0, p1, nx, p3)
                
        # 3번 말 이동 (대칭성 제거: p3 != p0, p1, p2)
        if p3 != 32 and p3 != p0 and p3 != p1 and p3 != p2:
            nx = MOVE[p3 * 6 + d]
            if nx == 32 or (nx != p0 and nx != p1 and nx != p2):
                dfs(depth + 1, total + SCORE[nx], p0, p1, p2, nx)

    # 시작 상태
    dfs(0, 0, 0, 0, 0, 0)
    print(ans)

if __name__ == '__main__':
    solve()