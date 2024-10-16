# [ ] 400 다이나믹프로그래밍 1
# 손이나 머리로 규칙성을 찾고, 코드로 만들기


# 1로 만들기
# N-> 1 의 최소 연산이 아니라 1-> N을 만드는데 최소 횟수만 사용하도록 연산
# 1부터 N까지 세가지 연산을 이용해서 각 수를 만들 수 있는 최소 연산을 누적하여 최소 연산 값 찾기
'''
N = int(input())

# dp 초기화
dp = [0 for i in range(N+1)]

# dp 채우기
for i in range(2,N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0 :
        dp[i] = min (dp[i], dp[i//2]+1)
    if i % 3 == 0 :
        dp[i] = min (dp[i], dp[i//3]+1)
print(dp[N])
'''

# 2×n 타일링

# 2×n 타일링 2

# 1, 2, 3 더하기
# 내 풀이 :  창의적이지만, 성능이 많이 떨어집니다.
# import itertools

# T = int(input())
# data = [1, 2, 3]

# for _ in range(T):
#     n = int(input())
#     count = 0
#     # Generate permutations allowing repetition
#     for i in range(1,n+1):
#         permutations = itertools.product(data, repeat=i)

#         for perm in permutations:
#             if sum(perm) == n: 
#                 count += 1
#     print(count)


# GPT 
T = int(input())
cases = [int(input()) for _ in range(T)]

# dp 배열 준비
dp = [0] * 12  # n이 11보다 작으므로 dp[0]부터 dp[10]까지 필요
dp[0] = 1  # 기본 사례: 0을 만드는 방법 1개

# dp 배열 채우기
for i in range(1, 11):
    dp[i] = dp[i - 1]
    if i >= 2:
        dp[i] += dp[i - 2]
    if i >= 3:
        dp[i] += dp[i - 3]

# 각 테스트 케이스에 대한 결과 출력
for n in cases:
    print(dp[n])

# 카드 구매하기

# 카드 구매하기 2

# 1, 2, 3 더하기 5

# 쉬운 계단 수

# 이친수

# 가장 긴 증가하는 부분 수열

# 가장 긴 증가하는 부분 수열 4

# 연속합

# 제곱수의 합

# 합분해

# 1, 2, 3 더하기 3

# RGB거리

# 동물원

# 오르막 수

# 스티커

# 포도주 시식

# 정수 삼각형

# 가장 큰 증가 부분 수열

# 가장 긴 감소하는 부분 수열

# 가장 긴 바이토닉 부분 수열

# 연속합 2

# 타일 채우기