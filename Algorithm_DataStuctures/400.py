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
import itertools

def defind_permutation(nums):
    permutation = itertools.permutations(nums)
    print(set(permutation))
defind_permutation([1,2,3,4])    

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