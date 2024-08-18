# TODO: 알고리즘 개요 

# 무엇이 좋은 알고리즘인가 ?:
# 정확성, 작업량, 메모리 사용량 , 단순성, 최적성 

# 시간 복잡도 
# O(2n+1) -> 최고차항만 생각, 계수 제거 -> O(n)

# YES, Python is Slow, and I Don't care.
# A rant on sacrificing performance for productivity.

# [ ]:배열과 리스트의 차이점 
# 리스트 크기가 가변적이고, 다양한 데이터를 저장할 수 있다.

# [ ] 슬라이싱, 시퀀스 자료형의 원하는 범위를 선택하는 연산 

# [ ]함수와 연산 
# 소속하는지 2 in [1,2,3] -> TRUE, 소속하지 않은지 2 not in [2,3,4] FALSE
# Insert : 해당 위치에 삽입 a.insert(index,value)
# POP : 특정 인덱스 항목 삭제 a.pop(index)
# remove : 특정 값을 삭제 (첫번쨰값만) a.remove(value)
# Count : 일치하는 값의 개수. a = [9,4,4,4,9,5,9] a.count(9)

a= [2,4,5,2,2]
print(a.count(2))
a.remove(2)
print(a) 

# 리스트 함축 
my_list = [2,3,4,5,6]
my_list = [i for i in my_list if i% 2 == 0 ]
print(my_list)