import sys
input = sys.stdin.readline

m, n = map(int, input().split())

# 1. 처음에 모든 수가 소수(True)라고 가정하고 리스트 생성
# 0번, 1번 인덱스는 안 쓰거나 False 처리 (0, 1은 소수가 아님)
array = [True] * (n + 1)
array[0] = False
array[1] = False

# 2. 에라토스테네스의 체
# 2부터 n의 제곱근까지만 검사하면 됨 (수학적 증명에 의해)
for i in range(2, int(n**0.5) + 1):
    if array[i]:  # i가 소수라면
        # i의 배수들을 모두 지움 (False로 변경)
        # i*2 부터 시작해도 되지만, i*i 부터 시작하는 게 더 효율적
        # step을 i로 설정하여 배수만 순회
        for j in range(i * i, n + 1, i):
            array[j] = False

# 3. M부터 N까지 살아남은(True) 수 출력
for i in range(m, n + 1):
    if array[i]:
        print(i)