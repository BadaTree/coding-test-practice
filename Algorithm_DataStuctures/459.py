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

# [ ] 10039 평균 점수 
'''
total = 0

for _ in range(5):
    score = int(input())
    total += score  if score >= 40 else 40
print(total //5)
'''

# [ ] 5063 TGN
'''
import sys

input = sys.stdin.read().splitlines()

N = int(input[0])

for i in range(1,N+1):
    case = list(map(int,input[i].split()))
    
    if case[0] < case[1] - case[2]:
        print("advertise")
    elif case[0] > case[1] - case[2]:
        print("do not advertise")
    else : 
        print("does not matter")
'''        

# [ ] 10886 0 = not cut / 1 =cute
'''
import sys

input = sys.stdin.read().splitlines()

N = int(input[0])
cute_votes = 0

for i in range(1, N+1):
    opinion = input[i]
    
    cute_votes += 1 if opinion == '1' else -1
    
print("Junhee is cute!" if cute_votes > 0 else "Junhee is not cute!")
'''
# [ ] 5717 상근이의 친구들

'''
while  True :
    friends = input()
    
    if friends == "0 0":
        break
    
    M, F = map(int,friends.split())
    print(M+F)
'''

# [ ] 9610 사분면
'''
import sys

input = sys.stdin.read().splitlines()

N = int(input[0])
points = [0]* 5

for i in range(1,N+1):
    x,y = map(int, input[i].split())
    
    if x == 0 or y == 0 :
        points[0] += 1
    elif x > 0 and y > 0 :
        points[1] += 1
    elif x < 0 and y > 0 :
        points[2] += 1
    elif x < 0 and y < 0 :
        points[3] += 1
    elif x > 0 and y < 0 :
        points[4] += 1
        
for i in range(1,5):
    print(f"Q{i}: {points[i]}")

print(f"AXIS: {points[0]}")

'''

# [ ] 10162 전자레인지
'''
T = int(input())
A,B,C = 0,0,0

if T >= 300 :
    cnt = T // 300
    T = T % 300
    A += cnt

if T >= 60 :
    cnt = T // 60
    T = T % 60
    B += cnt
    
if T >= 10 :
    cnt = T // 10
    T = T % 10
    C += cnt
    
print (f"{A} {B} {C}" if T == 0 else -1)

# GPT
T = int(input())
A, B, C = 0, 0, 0

if T >= 300:
    A = T // 300
    T %= 300

if T >= 60:
    B = T // 60
    T %= 60

if T >= 10:
    C = T // 10
    T %= 10

# 결과 출력
if T == 0:
    print(f"{A} {B} {C}")
else:
    print(-1)
'''

# [ ] 10214 Baseball
'''
import sys

scores = sys.stdin.read().splitlines()

T = int(scores[0])
Y = 0
K = 0

for i in range(1,T+1):
    y,k = map(int, scores[i].split())
    
    Y += y 
    K += k

if Y == K :
    print("Draw")
else:
    if Y > K :
        print("Yonsei")
    else :
        print("Korea")
'''

# GPT 
'''
import sys

# 입력 전체를 읽고 각 줄을 나눔
scores = sys.stdin.read().splitlines()

# 첫 번째 줄은 테스트 케이스의 수
T = int(scores[0])

# 인덱스를 사용해서 각 테스트 케이스의 데이터를 처리
index = 1
for _ in range(T):
    Y, K = 0, 0
    # 9회차 점수 읽기
    for _ in range(9):
        y, k = map(int, scores[index].split())
        Y += y
        K += k
        index += 1
    
    # 결과 출력
    if Y > K:
        print("Yonsei")
    elif Y < K:
        print("Korea")
    else:
        print("Draw")
'''


# [ ] 10103 주사위 게임
'''
import sys

scores = sys.stdin.read().splitlines()

chang = 100
sang = 100

R = int(scores[0])

for i in range(1,R+1):
    c,s = map(int,scores[i].split())
    if c < s :
        chang -= s
    elif c > s :
        sang -= c
        
print(chang)
print(sang)
'''

# [ ] 10102 개표
'''
V = int(input())
votes = input()

A = votes.count('A')
B = V - A
if A == B :
    print('Tie')
elif A > B :
    print('A')
else :
    print('B')
'''

# [ ] 7567 그릇 
'''
bowl = input()
height = 10
for i in range(1,len(bowl)):
    if bowl[i-1] == bowl[i]:
        height += 5
    else :
        height += 10
print(height)
'''

# [ ] 5355 화성 수학

import sys

input = sys.stdin.read().splitlines()
T = int(input[0])

for i in range(1,T+1):
    cal_list = input[i].split()
    n = float(cal_list[0])
    result = n
    
    for j in cal_list:
        if j == '@':
            result *= 3
        elif j == '%':
            result += 5
        elif j == '#':
            result -= 7
    print(f"{result:.2f}")