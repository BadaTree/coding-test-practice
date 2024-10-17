# [ ] Python 배우기 
# https://www.acmicpc.net/workbook/view/459

# [ ] 11653 소인수 분해
'''
N = int(input())
for i in range(2,N+1):
    if N == 0 :
        break
    
    while N % i == 0:
        N //= i 
        print(i)
        
# GPT 

import math

N = int(input())

# 먼저 2로 나누어지면 나누기
while N % 2 == 0:
    print(2)
    N //= 2

# 그 다음 3 이상의 홀수만 검사
for i in range(3, int(math.sqrt(N)) + 1, 2):
    while N % i == 0:
        print(i)
        N //= i

# 만약 N이 1보다 크면 그것은 소수임
if N > 1:
    print(N)
'''

# [ ] 1789 수들의 합
# 최대한 많은 수를 이용해서 S를 만들고자할 때

# print(len([i for i in range(1,20)]))


# [ ] 10156 과자
'''
K, N , M = map(int,input().split())
print(K*N - M if K*N - M > 0 else 0)
'''
# [ ] 3046 R2
'''
R1,S = map(int,input().split())

print(S*2 - R1)
'''