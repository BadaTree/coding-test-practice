# TODO: 7강 기본 입출력 ~ 8 강 조건문 (앞강이 너무 길어져서 분리)

# NOTE: 자주 사용되는 입출력 
# input() 한 줄의 문자영을 입력 받는 함수.
# map() 리스트의 모든 원소에 각각 특정한 함수를 적용할 떄 사용.

#a = list(map(int,input().split()))
##a,b,c = map(int, input().split()) # 입력이 많지 않을 때

# n명의 학생의 성적을 입력 받아 내림차순으로 정렬
n = int(input())

if n >= 3 :
    score = list(map(int, input().split()))
    print(score)
else:
    a,b = map(int,input().split())
    print(a,b)

# 즉 입력의 갯수가 정해져있을 떄, a,b,c = map(int, input().split())
# 입력의 갯수가 랜덤일 때, list = list(map(int, input().split()))

# NOTE: 빠르게 입력받기
import sys

data = sys.stdin.readline().rstrip()
print(data)

# TIP: 자주 사용되는 표준 출력 방법
a,b,c = 2,3,4
print(a,b)
print(c, end=" ")
# NOTE: f-string 방식
print(f'출력문의 기본 속성의 줄바꿈을 바꾸어 주고 싶다면 end= 선언해줍니다{a,b,c}')

# TIP: 조건문 
# 논리 연산자 조건, a,b가 존재할 떄 둘 다 참이면 a and b, 둘 중 하나가 참일 때 참 a or b, a가 거짓일 때 참: not a 

# NOTE: 기타 연산자  x in list , x not in list 
# list 안에 x가 포함될 떄 참. 리스트 , 튜플, 문자열, 딕셔너리에서 모두 사용
# NOTE: 아무것도 처리하고 싶지 않을 떄 pass 
if True:
    pass

# NOTE: 조건문의 간소화
if True or False : print('WOW')
else: print('EWWW')

score = 80 

result = "P" if score>70 else "NP"
print(f"i got {result} ")

# NOTE: 파이썬 조건문 내에서의 부등식 
# 0 < x and x < 10 == 0 < x < 10