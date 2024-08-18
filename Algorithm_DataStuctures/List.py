#TODO: 7강 기본 입출력까지 공부하기 


#TODO: 4강ㅣ리스트 자료형
# TIP: 2차원 배열 초기화의 좋은/나쁜 예시 초기화할 떄 주의하기

m = 3
n = 5

array = [[0]*m for _ in range(n)]
print(f'좋은 예시의 결과 입니다{array}')
array[1][1] = 100
print(f'올바른 초기화의 값 변경 결과 {array}')

array = [[0]*m]*n
print(f'안 좋은 예시의 결과 입니다{array}')
array[1][1] = 100
print(f'전체 리스트가 하나의 객체로 인식되어 리스트 전체의 값이 바뀜 {array}')

# TIP: 리스트 관련 기타 메서드 
sample_array = [i+1 for i in range(6)]
sample_array.append(50)
sample_array.sort(reverse=True)
print(sample_array.count(300)) # NOTE: list의 총 데이터의 개수를 계산하는 것이 아니라 리스트에 특정값의 개수를 카운트

sample_array.insert(3,300)
print(f'3번 인덱스에 300을 추가 {sample_array}')

sample_array.remove(3) # NOTE: 해당 인덱스의 값을 제거하는 것이 아니라, 특정한 값을 찾아 제거하는 것임 !! 
print(sample_array)

# 리스트에서 특정 조건 값 삭제하기 
a = [22,30,40,45,65,43,22,13,22]
result_set = [40,45]

result = [i for i in a if i>=30]
print(f'30 이상인 값만 포함된 리스트 {result}')
result = [i for i in a if i%2 != 0]
print(f'홀수인 값만 포함된 리스트 {result}')
result = [i for i in a if i != 22]
print(f'22가 제거된 리스트 {result}')
result = [i for i in a if i not in result_set]
print(f'특정 리스트의 값을 모두 제거한 리스트  {result}')
