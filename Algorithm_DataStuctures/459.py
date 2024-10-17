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

# [ ] 10699 오늘 날짜
'''
from datetime import datetime, timedelta

current_time = datetime.utcnow() + timedelta(hours=9)
print(current_time.strftime("%Y-%m-%d"))
'''

# [ ] 2914 저작권
# 앨범에 수록된 수 A, I = 멜로디 수 / 수록된 수 (A)가 주어질 때, 최소한의 멜로디의 수 A*(I-1)+1
'''
A, I = map(int, input().split())

print(A*(I-1)+1)
'''

# [ ] 2754 학점 계산 
'''
score_dict = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
'F': 0.0}

score = input()
print(score_dict[score])
'''


# [ ] 2476 주사위 게임 \
'''
import sys

input = sys.stdin.read().strip().splitlines()
n = int(input[0])
final_award = 0 

for i in range(1,n+1):
    award = 0
    a,b,c = map(int,input[i].split())
    # 세 개가 모두 같은 눈일 때
    if len(set([a,b,c])) == 1:
        award = 10000 + a*1000
    # 두 개가 모두 같은 눈일 때
    elif len(set([a,b,c])) == 2:
        same = 0
        for i in (a,b,c):
            same ^= i
        award = 1000 + (a+b-same)*100
    # 세 개가 모두 다른 눈일 때
    else :
        award = max([a,b,c])* 100 

    if award > final_award :
        final_award = award

print(final_award)
'''
'''
import sys

input = sys.stdin.read().strip().splitlines()
n = int(input[0])
final_award = 0 

for i in range(1,n+1):
    award = 0
    a,b,c = map(int,input[i].split())
    # 세 개가 모두 같은 눈일 때
    if a==b==c:
        award = 10000 + a*1000
    # 두 개가 모두 같은 눈일 때
    elif a==b or b == c or a==c:
        if a ==b or a==c :
            award = 1000 + a*100
        else : 
            award = 1000 + b*100
    # 세 개가 모두 다른 눈일 때
    else :
        award = max([a,b,c])* 100 
        
    final_award = max(final_award,award)

print(final_award)
'''