# TODO: 파이썬 반복문과 기본 문법 및 라이브러리에 대해 학습.

# TIP: 반복문 (while, for)

list = [1,2,3,4]
for i in list :
    print(i)


for i in range(1,5): # NOTE: range(시작 값, 끝 값+1), range(4) == rangr(0,4)
    print(i)

for i in range(1,5):
    if i % 2 == 0 :
        continue #NOTE: 반복문에서 아래 남은 코드 건너뛰고, 반복문 탈출
    print(i)

# 부정행위 대상자를 제외한 합격(80 이상)생 명단 출력하기 
score = [90,85,77,65,97]
student_list = {2,4}

for i in range(1,6): 
    if i in student_list:
        continue
    if score[i-1] >= 80:
        print(f'{i}번 학생은 합격입니다.')


# TIP: 함수와 란다 표현식 
# 내장 함수 : 기본제공함수, 사용자 정의 함수 : 사용자가 정의하는 함수 
def change_to_k(a):
    print(f'{a}k는 {a*1000}을 의미합니다.')
print(change_to_k(8))

# NOTE: global 키워드 지역변수로 만들지 않고, 외부 변수를 참조. 전역변수를 수정할 때 필요함.
# 동일한 전역/지역 변수가 있을 때, 함수 내부는 지역변수로, 함수 외부는 전역변수가 출력된다.

a = 0

def flus():
    global a
    a += 1

for i in range(10):
    flus() 

print(a)

# TIP: 여러 개의 반환값 가지기 
def operator(a,b):
    sum = a+b
    sub = a-b
    mult = a*b
    return sum, sub, mult #NOTE: 패킹, 한꺼번에 반환

a,b,c = operator(10,7) # NOTE: 언패킹, 반환 값을 차례대로 특정 변수에 담기


# TIP: 람다 표현식 : 이름없는 함수 . 특정한 기능의 함수를 한 줄에 표현 
# NOTE: 함수가 매우 간단하거나 한번 사용되는 경우 유용 

def add(a,b):
    print(a+b)

print(add(3,3))

print((lambda a,b: a+b)(3,3))
print((lambda a,b: a*b)(3,3))

# TIP:  SORTED 
array = [('하늘',60),('바다',30),('지혜',40)]

def key(x):
    return x[1]

print(sorted(array, key=key))
print(sorted(array, key=(lambda x: x[1])))

# TIP:  여러 개의 리스트에 적용

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

#result = map(lambda a, b: a + b, list1, list2)

#result_list = list(result)  # Convert the map object to a list

#print(result_list[1])  # Print the second element of the resulting list


# TIP: 실전에서 유용한 라이브러리 
# intertools : 반복되는 형태의 데이터를 처리하기 위한 유용한 기능을 제공한다.(순열,조합)
# heapq: 힙 자료구조를 제공한다 (큐 기능을 구현하기 위해 제공한다.)
# bistect: 이진탐색 기능을 제공한다.
# collections : 덱, 카운터 등의 유오ㅛㅇ한 자료구조를 포함한다.
# math : 필수적인 수학적 기능을 제공한다.

print(f'합은{sum(list1)}') # 합을 계산해줌 
print(f'최대{max(1,3,6,8,9)}, 최소{min(2,1,-5,5)}') #최대 최소 계산
print(f'계산 결과를 상수로 반환 {eval("3*3*3")}')

# Sorted()
result = sorted([9,2,5,7,1]) # 오름차순
print(result)
result = sorted([9,2,5,7,1], reverse=True) # 내림차순
print(result)

# Sotrte() with Key 
array = [('하늘',60),('바다',30),('지혜',40)]
print(sorted(array, key=(lambda x: x[1])))

# TIP:  순열. 서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것 

from itertools import permutations

data = ['a', 'b', 'c']

result = list(permutations(data, 3))  # 변경된 변수명을 사용하여 호출

print(result)

# TIP:  조합. 서로 다른 n개에서 r개를 선택하여 순서관계없이 나열하는 것 

from itertools import combinations

data = ['a', 'b', 'c']

result = list(combinations(data, 3))  # 변경된 변수명을 사용하여 호출

print(result)

# TIP: 중복 순열 : product, 중복 조합 : combinations_with_replacement

# TIP: Counter , 원소의 등장 횟수 반황
from collections import Counter

list_rgb = ['R','R','R','b','b','b','G']

counter = Counter(list_rgb)
print(counter['R'],counter['b'],counter['G'])